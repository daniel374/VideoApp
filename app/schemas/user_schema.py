from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    name_usr: str
    email_usr: str = Field(..., pattern=r'^\S+@\S+\.\S+$', description="Email de Usuario")


class UserResponse(BaseModel):
    id_usr: int
    name_usr: str
    email_usr: str

    model_config = ConfigDict(from_attributes=True)