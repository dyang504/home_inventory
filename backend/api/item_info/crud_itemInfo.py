from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime

from backend.lib.crud_base import CRUDBase
from backend.db.models import Item_info
from .iteminfo_schema import ItemInfoCreate, ItemInfoUpdate


class CRUDItemInfo(CRUDBase[Item_info, ItemInfoCreate, ItemInfoUpdate]):
    def get_iteminfos_with_user_and_item(self, db: Session, user_id: int,
                                         item_id: int) -> List[Item_info]:
        return db.query(self.model).filter(
            (Item_info.user_id == user_id)
            and (Item_info.item_id == item_id)).all()

    def create_iteminfos_with_user_and_item(self, db: Session, *,
                                            obj_in: ItemInfoCreate,
                                            user_id: int,
                                            item_id: int) -> Item_info:
        obj_in_data = dict(obj_in)
        db_obj = self.model(**obj_in_data,
                            user_id=user_id,
                            item_id=item_id,
                            create_at=datetime.now(),
                            update_at=None)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


item_info = CRUDItemInfo(Item_info)
