from pydantic import BaseModel, HttpUrl


class UserIcon(BaseModel):
    image_url: HttpUrl

    class Config:
        orm_mode = True


class UserIconCreate(UserIcon):
    user_id: int


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdate(UserBase):
    username: str
    email: str


class UserOut(UserBase):
    id: int
    username: str
    email: str
    icon: UserIcon = None
