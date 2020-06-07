from sqlalchemy.orm import Session
from datetime import datetime

from backend.crud.base import CRUDBase
from backend.db.models import Item_image
from backend.schema.item_image_schema import ItemImageCreate, ItemImageUpdate


class CRUDItemImage(CRUDBase[Item_image, ItemImageCreate, ItemImageUpdate]):
    pass


item_image = CRUDItemImage(Item_image)
