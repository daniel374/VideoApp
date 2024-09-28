# schemas.py
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class CommentCreate(BaseModel):
    detail_cmt: str = Field(..., min_length=1, max_length=500, description="The comment content")


class CommentResponse(BaseModel):
    id_cmt: int
    detail_cmt: str
    date_cmt: datetime

    model_config = ConfigDict(from_attributes=True)
