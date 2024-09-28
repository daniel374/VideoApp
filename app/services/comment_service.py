# services/comment_service.py
from sqlalchemy.orm import Session
from app.models import Comments, Video


class CommentService:
    def __init__(self, db: Session):
        self.db = db

    def get_comments_for_video(self, id_vd: int):
        return self.db.query(Comments).filter(Comments.id_video_cmt == id_vd).all()

    def add_comment_to_video(self, id_vd: int, comment_data: dict):
        new_comment = Comments(**comment_data, id_video_cmt=id_vd)
        self.db.add(new_comment)
        self.db.commit()
        self.db.refresh(new_comment)
        return new_comment
