from pydantic import BaseModel, ConfigDict
from typing import List
from .video_schema import VideoResponse
from .thumbnail_schema import ThumbnailResponse


class VideoThumnailResponse(BaseModel):
    videos: List[VideoResponse]
    thumbnails: List[ThumbnailResponse]

    model_config = ConfigDict(from_attributes=True)