from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime

from backend.lib.crud_base import CRUDBase
from backend.db.models import Inventory_location
from .inventory_location_schema import (InventoryLocationCreate,
                                        InventoryLocationUpdate)


class CRUDInventoryLocation(CRUDBase[Inventory_location,
                                     InventoryLocationCreate,
                                     InventoryLocationUpdate]):
    def get_inventory_location_by_user(self, db: Session, user_id: int):
        locations = db.query(
            self.model).filter(self.model.user_id == user_id).all()
        return locations

    def create_inventory_location_by_user(self, db: Session,
                                          obj_in: InventoryLocationUpdate,
                                          user_id: int):
        obj_in_data = jsonable_encoder(obj_in)
        new_location = Inventory_location(**obj_in_data, user_id=user_id)
        db.add(new_location)
        db.commit()
        db.refresh(new_location)
        return new_location


inventory_location = CRUDInventoryLocation(Inventory_location)
