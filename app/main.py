from fastapi import FastAPI, HTTPException, BackgroundTasks, Request, Form, Depends, APIRouter, Query
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime

from app import models, database

from typing import List, Optional
import os
import asyncio
import uvicorn

from app.models import Video, Likes
from app.schemas.combined_response import VideoThumnailResponse
from app.schemas.likes_schema import LikeCreate
from app.schemas.thumbnail_schema import ThumbnailResponse, ThumbnailCreate
from app.schemas.user_schema import UserCreate
from app.schemas.video_schema import VideoResponse, VideoCreate, VideoSearch
from app.services.comment_service import CommentService
from app.services.likes_service import LikesService
from app.services.thumbnail_service import ThumbnailService
from app.services.user_service import UserService
from app.services.video_service import VideoService
from app.services.video_thumbnail_service import VideoThumbnailService
from app.utils import *

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:3000" #URL Frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#path storage thumbnail
THUMBNAIL_DIR = "static/images/thumbnail"
# path  storage videos
VIDEO_DIR = "static/videos"

# Ruta para servir archivos estaticos
# Pytest
#app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Run and Debug
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates
templates = Jinja2Templates(directory="templates")
# Data Example
artists = ["Artista 1", "Artista 2", "Artista 3"]


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    db_user = models.User(name_usr=user.name_usr, email_usr=user.email_usr)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/")
def read_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@app.get("/", response_model=List[VideoThumnailResponse])
def list_videos(request: Request, db: Session = Depends(database.get_db)):
    service = VideoThumbnailService(db)
    videos, thumbnails = service.get_videos_and_thumbnails()
    video_thumbnail_pairs = zip(videos, thumbnails)
    if not isinstance(videos, list):
        videos = [videos]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "videos": videos,
        "thumbnails": thumbnails,
        "video_thumbnail_pairs": video_thumbnail_pairs,
        "artists": artists
    })


@app.get("/videos/", response_model=List[VideoResponse])
def list_videos(db: Session = Depends(database.get_db)):
    service = VideoService(db)
    return service.list_videos()


@app.post("/videos/", response_model=VideoResponse)
def create_video(video_data: VideoCreate, db: Session = Depends(database.get_db)):
    service = VideoService(db)
    return service.create_video(video_data)


@app.post("/thumbnails/", response_model=ThumbnailResponse)
def create_video(thumbnail_data: ThumbnailCreate, db: Session = Depends(database.get_db)):
    service = ThumbnailService(db)
    return service.create_thumbnail(thumbnail_data)


@app.get("/videos/{id_vd}", name="show_video")
def show_video(id_vd: int, request: Request, db: Session = Depends(database.get_db)):

    video = db.query(Video).filter(Video.id_vd == id_vd).first()

    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")

    video_service = VideoService(db)
    # Obtener videos relacionados (esto es solo un ejemplo, puedes usar alguna lógica de recomendación)
    related_videos = video_service.get_related_videos(id_vd)

    return templates.TemplateResponse("video_detail.html", {
        "request": request,
        "video": video,
        "related_videos": related_videos
    })


@app.post("/videos/{video_id}/comments")
def add_comment_to_video(video_id: int, detail_cmt: str = Form(...), db: Session = Depends(database.get_db)):
    comment_service = CommentService(db)
    comment_data = {"detail_cmt": detail_cmt}
    comment_service.add_comment_to_video(video_id, comment_data)
    return RedirectResponse(url=f"/videos/{video_id}", status_code=303)


@app.get("/search/", response_model=List[VideoSearch])
def search_videos(request: Request, search: str, filtro: str, db: Session = Depends(database.get_db)):
    video_service = VideoService(db)
    author_service = UserService(db)

    if filtro == "Titulo":
        # Filtrar por título
        results = video_service.search_videos(search)
    elif filtro == "Author":
        # Filtrar por autor
        results = author_service.search_by_author(search)
    else:
        results = video_service.search_videos(search)
    # Obtener videos relacionados (esto es solo un ejemplo, puedes usar alguna lógica de recomendación)
    if not results:
        raise HTTPException(status_code=404, detail="No videos found matching your criteria.")
    else:
        related_videos = video_service.get_related_videos(results[0].id_vd)

    return templates.TemplateResponse("video_detail.html", {
        "request": request,
        "video": results[0],
        "related_videos": related_videos
    })


@app.post("/videos/{id_vd}/like")
def handle_like(id_vd: int, like_data: LikeCreate, db: Session = Depends(database.get_db)):
    video = db.query(Video).filter(Video.id_vd == id_vd).first()

    like_service = LikesService(db)
    likes = like_service.list_likes_for_video(id_vd)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    # Aquí podrías incluir la lógica para verificar si el usuario ya ha dado like/dislike.
    if like_data.video_lk:
        num_video_lk = likes.num_video_lk + 1
    else:
        num_video_lk = likes.num_video_lk - 1

    lvideo_service = VideoService(db)
    like = Likes(
        video_lk=like_data.like,
        id_user_lk=like_data.user_id,
        id_video_lk=id_vd,
        num_video_lk=num_video_lk
    )

    db.add(like)
    db.commit()
    return {"message": "Like added"}

#Para visualizar los path de las rutas que tenemos configuradas:
"""
for route in app.routes:
    print(route.name, route.path)
"""

async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())