# app/repositories/video_repository.py
from sqlalchemy.orm import Session
from app.models import Video
from app.schemas.video_schema import *


class VideoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_videos(self):
        return self.db.query(Video).all()

    def get_video_by_id(self, video_id: int):
        return self.db.query(Video).filter(Video.id_vd == video_id).first()

    def create_video(self, video_data: VideoCreate):
        new_video = Video(
            name_vd=video_data.name_vd,
            url_vd=video_data.url_vd,
            description_vd=video_data.description_vd,
            id_autor_vd=video_data.id_autor_vd
        )
        self.db.add(new_video)
        self.db.commit()
        self.db.refresh(new_video)
        return new_video