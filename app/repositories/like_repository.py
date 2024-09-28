from sqlalchemy.orm import Session
from app.models import Likes
from app.schemas.likes_schema import *


class LikeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_likes(self):
        return self.db.query(Likes).all()

    def add_like(self, like_data: LikeCreate):
        like_dislike = Likes(**like_data.dict())
        self.db.add(like_dislike)
        self.db.commit()
        self.db.refresh(like_dislike)
        return like_dislike

    def get_likes_for_video(self, id_vd: int):
        # Obtener likes para un video específico
        return self.db.query(Likes).filter(Likes.id_video_lk == id_vd).all()
