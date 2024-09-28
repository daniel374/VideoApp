from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


# Esquema para crear un nuevo video
class VideoCreate(BaseModel):
    name_vd: str
    url_vd: str
    description_vd: Optional[str] = None
    id_autor_vd: Optional[int] = None


class VideoResponse(BaseModel):
    id_vd: int
    name_vd: str
    url_vd: str
    date_vd: datetime
    description_vd: Optional[str] = None
    id_autor_vd: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class VideoSearch(BaseModel):
    query: str = Field(..., min_length=1, description="Buscar video por nombre")
