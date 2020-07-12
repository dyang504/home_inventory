from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    pass