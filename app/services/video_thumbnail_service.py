from sqlalchemy.orm import Session
from .thumbnail_service import ThumbnailService
from .video_service import VideoService


class VideoThumbnailService(VideoService):
    def __init__(self, db: Session):
        self.video_service = VideoService(db)
        self.thumbnail_service = ThumbnailService(db)

    def get_videos_and_thumbnails(self):
        videos = self.video_service.list_videos()
        thumbnails = self.thumbnail_service.list_thumbnails()
        return videos, thumbnails

    def get_video_and_thumbnail_by_id(self, id_vd_thn: int):
        video = self.video_service.get_video(id_vd_thn)
        thumbnail = self.thumbnail_service.get_thumbnail(id_vd_thn)
        return video, thumbnail
