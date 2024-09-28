from app.models import Video
from app.repositories.video_repository import VideoRepository
from app.schemas.video_schema import VideoCreate, VideoResponse
from sqlalchemy.orm import Session


class VideoService:
    def __init__(self, db: Session):
        self.video_repository = VideoRepository(db)
        self.db = db

    def list_videos(self):
        return self.video_repository.get_all_videos()

    def get_video(self, id_vd: int):
        return self.video_repository.get_video_by_id(id_vd)

    def create_video(self, video_data: VideoCreate):
        return self.video_repository.create_video(video_data)

    def get_related_videos(self, id_vd: int):
        return self.db.query(Video).filter(Video.id_vd != id_vd).limit(3).all()

    def search_videos(self, search_term: str):
        search_pattern = f"%{search_term}%"
        return self.db.query(Video).filter(Video.name_vd.like(search_pattern)).all()
