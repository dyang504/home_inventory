from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime

from backend.crud.base import CRUDBase
from backend.db.models import Status
from backend.schema.status_schema import StatusCreate, StatusUpdate


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    def create_status_with_owner(self, db: Session, obj_in: StatusCreate,
                                 user_id: str) -> Status:
        status = Status(name=obj_in.name, user_id=user_id)
        db.add(status)
        db.commit()
        db.refresh(status)
        return status


status = CRUDStatus(Status)
