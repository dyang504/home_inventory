from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime

from backend.crud.base import CRUDBase
from backend.db.models import Status
from backend.schema.status_schema import StatusCreate, StatusUpdate


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    pass


status = CRUDStatus(Status)
