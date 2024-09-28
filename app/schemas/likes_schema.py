from pydantic import BaseModel, ConfigDict
from typing import Optional


class LikeCreate(BaseModel):
    id_video_lk: int
    isLike: Optional[int] = None
    num_video_lk: Optional[int] = None
    id_user_lk: Optional[int] = None


class LikesResponse(BaseModel):
    id_lk: int
    num_video_lk: int
    id_user_lk: int
    id_video_lk: int

    model_config = ConfigDict(from_attributes=True)