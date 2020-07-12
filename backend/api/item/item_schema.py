from typing import List, Optional

from pydantic import BaseModel
from ..item_info.iteminfo_schema import ItemInfoCreate, ItemInfoOut, ItemInfoUpdate
from ..item_image.item_image_schema import ItemImageCreate, ItemImageUpdate
from ..nutrition.nutrition_schema import NutritionCreate, NutritionUpdate
from ..category.category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from ..size.size_schema import SizeCreate, SizeUpdate
from ..book_property.book_property_schema import BookPropertyCreate, BookPropertyUpdate


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
