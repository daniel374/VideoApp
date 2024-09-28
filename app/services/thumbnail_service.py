from app.repositories.thumbnail_repository import ThumbnailRepository
from app.schemas.thumbnail_schema import ThumbnailCreate, ThumbnailResponse
from sqlalchemy.orm import Session


class ThumbnailService:
    def __init__(self, db: Session):
        self.thumbnail_repository = ThumbnailRepository(db)

    def list_thumbnails(self):
        return self.thumbnail_repository.get_all_thumbnails()

    def get_thumbnail(self, id_thn: int):
        return self.thumbnail_repository.get_thumbnail_by_id(id_thn)

    def create_thumbnail(self, thumbnail_data: ThumbnailCreate):
        return self.thumbnail_repository.create_thumbnail(thumbnail_data)