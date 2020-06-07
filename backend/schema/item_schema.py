from typing import List, Optional

from pydantic import BaseModel
from backend.schema.iteminfo_schema import ItemInfoCreate, ItemInfoOut, ItemInfoUpdate
from backend.schema.item_image_schema import ItemImageCreate, ItemImageUpdate
from backend.schema.nutrition_schema import NutritionCreate, NutritionUpdate
from backend.schema.category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from backend.schema.size_schema import SizeCreate, SizeUpdate
from backend.schema.book_property_schema import BookPropertyCreate, BookPropertyUpdate


class ItemBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass
    # infos: List[ItemInfoCreate] = []
    # nutritions: List[Optional[NutritionCreate]]
    # images: Optional[ItemImageCreate]
    # category: CategoryCreate
    # size: Optional[SizeCreate]
    # book_property: Optional[BookPropertyCreate]


class ItemCreateAll(ItemBase):
    infos: List[ItemInfoCreate] = []
    nutritions: List[Optional[NutritionCreate]]
    images: Optional[List[ItemImageCreate]]
    category: List[CategoryCreate]
    size: Optional[List[SizeCreate]]
    book_property: Optional[BookPropertyCreate]


class ItemUpdate(ItemBase):
    infos: List[ItemInfoUpdate]
    nutritions: List[Optional[NutritionUpdate]]
    images: Optional[List[ItemImageUpdate]]
    category: List[CategoryUpdate]
    size: Optional[List[SizeCreate]]
    book_property: Optional[BookPropertyUpdate]


class ItemOut(ItemBase):
    user_id: int
    infos: List[Optional[ItemInfoOut]]
    nutritions: List[Optional[NutritionCreate]]
    images: Optional[List[ItemImageCreate]]
    category: Optional[List[CategoryOut]]
    size: Optional[List[SizeCreate]]
    book_property: Optional[BookPropertyCreate]
