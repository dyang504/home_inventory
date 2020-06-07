from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime

from backend.crud.base import CRUDBase
from backend.db.models import Inventory_location
from backend.schema.inventory_location_schema import (InventoryLocationCreate,
                                                      InventoryLocationUpdate)


class CRUDInventoryLocation(CRUDBase[Inventory_location,
                                     InventoryLocationCreate,
                                     InventoryLocationUpdate]):
    pass


inventory_location = CRUDInventoryLocation(Inventory_location)
