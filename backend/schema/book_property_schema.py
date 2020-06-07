from typing import Optional
from pydantic import BaseModel


class BookPropertyBase(BaseModel):
    author: str
    publisher: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True


class BookPropertyCreate(BookPropertyBase):
    pass


class BookPropertyUpdate(BookPropertyBase):
    pass


class BookPropertyOut(BookPropertyBase):
    pass