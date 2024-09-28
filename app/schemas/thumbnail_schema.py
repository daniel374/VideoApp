from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class ThumbnailCreate(BaseModel):
    name_thn: str
    url_thn: str
    description_thn: Optional[str] = None
    id_video_thn: Optional[int] = None
    

class ThumbnailResponse(BaseModel):
    id_thn: int
    name_thn: str
    url_thn: str
    date_thn: datetime
    description_thn: Optional[str] = None
    id_video_thn: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)