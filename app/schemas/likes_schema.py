from pydantic import BaseModel, ConfigDict
from typing import Optional


class LikeCreate(BaseModel):
    video_lk: bool
    num_video_lk: int
    id_user_lk: int
    id_video_lk: int


class LikesResponse(BaseModel):
    id_lk: int
    video_lk: bool
    num_video_lk: int
    id_user_lk: int
    id_video_lk: int

    model_config = ConfigDict(from_attributes=True)