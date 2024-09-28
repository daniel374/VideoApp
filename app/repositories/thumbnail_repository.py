from sqlalchemy.orm import Session
from app.models import Thumbnail
from app.schemas.thumbnail_schema import *


class ThumbnailRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_thumbnails(self):
        return self.db.query(Thumbnail).all()

    def get_thumbnail_by_id(self, id_thn: int):
        return self.db.query(Thumbnail).filter(Thumbnail.id_thn == id_thn).first()

    def create_thumbnail(self, thumbnail_data: ThumbnailCreate):
        new_thumbnail = Thumbnail(
            name_thn=thumbnail_data.name_thn,
            url_thn=thumbnail_data.url_thn,
            description_thn=thumbnail_data.description_thn,
            id_video_thn=thumbnail_data.id_video_thn
        )
        self.db.add(new_thumbnail)
        self.db.commit()
        self.db.refresh(new_thumbnail)
        return new_thumbnail