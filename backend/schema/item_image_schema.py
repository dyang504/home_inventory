from typing import Optional

from pydantic import BaseModel


class ItemImageBase(BaseModel):
    image_url: Optional[str]

    class Config:
        orm_mode = True


class ItemImageCreate(ItemImageBase):
    pass


class ItemImageUpdate(ItemImageBase):
    pass


class ItemImageOut(ItemImageBase):
    pass