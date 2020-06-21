from typing import Optional
from pydantic import BaseModel, HttpUrl


class UserIcon(BaseModel):
    image_url: Optional[HttpUrl]

    class Config:
        orm_mode = True


class UserIconCreate(UserIcon):
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(UserBase):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    username: str
    email: str


class UserOut(UserBase):
    id: int
    username: str
    email: str
    icon: Optional[UserIcon] = None

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    password: str

    class Config:
        orm_mode = True