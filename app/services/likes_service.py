from sqlalchemy.orm import Session
from app.models import Likes, Video
from app.repositories.like_repository import LikeRepository
from app.schemas import likes_schema


class LikesService:
    def __init__(self, db: Session):
        self.like_repository = LikeRepository(db)
        self.db = db

    def list_likes(self, ):
        return self.like_repository.get_likes()

    def list_likes_for_video(self, id_vd: int):
        # Llamar al repositorio para obtener los likes de un video específico
        return self.like_repository.get_likes_for_video(id_vd)

    def list_videos_with_likes(self):
        # Obtener la lista de videos y asociar los likes a cada uno
        videos = self.db.query(Video).all()
        videos_with_likes = []
        for video in videos:
            likes = self.like_repository.get_likes_for_video(video.id_vd)
            video.likes = likes  # Asignar los likes al video
            videos_with_likes.append(video)
        return videos_with_likes

    def add_like_or_dislike_to_video(self, like_data: dict):
        new_like_dislike = Likes(**like_data)
        self.db.add(new_like_dislike)
        self.db.commit()
        self.db.refresh(new_like_dislike)
        return new_like_dislike