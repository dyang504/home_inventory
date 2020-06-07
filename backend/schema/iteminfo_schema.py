from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ItemInfoBase(BaseModel):
    price: float
    expiration_date: Optional[datetime]
    purchase_date: Optional[datetime]

    class Config:
        orm_mode = True


class ItemInfoCreate(ItemInfoBase):
    item_id: Optional[int]
    user_id: int
    status_id: Optional[int]
    inventory_location_id: Optional[int]


class ItemInfoUpdate(ItemInfoBase):
    pass


class ItemInfoDelete(ItemInfoBase):
    pass


class ItemInfo(ItemInfoBase):
    pass


class ItemInfoOut(ItemInfoBase):
    price: float
    expiration_date: Optional[datetime]
    purchase_date: Optional[datetime]
    create_at: Optional[datetime]
    update_at: Optional[datetime]
