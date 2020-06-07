from typing import List
from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.models import Status
from backend.schema.status_schema import StatusCreate, StatusUpdate, StatusOut
from backend.crud import crud_status

router = APIRouter()


@router.get("/status", response_model=List[StatusOut])
def read_status(db: Session = Depends(get_db)):
    db_obj = crud_status.status.get_multi(db=db)
    return db_obj


@router.post("/status/create", response_model=StatusOut)
def create_status(*, obj_in: StatusCreate, db: Session = Depends(get_db)):
    new_obj = crud_status.status.create(db=db, obj_in=obj_in)
    return new_obj


@router.put("/status/update", response_model=StatusOut)
def update_status(
    *, status_id: int, obj_in: StatusUpdate,
    db: Session = Depends(get_db)) -> StatusOut:
    db_obj = db.query(Status).filter(id == status_id).first()
    updated_obj = crud_status.status.update(db=db,
                                            obj_in=obj_in,
                                            db_obj=db_obj)
    return updated_obj


@router.delete("/status/delete")
def delete_status(*, status_id: int, db: Session = Depends(get_db)):
    db_obj = crud_status.status.remove(db=db, id=status_id)
    if db_obj:
        return {"code": 204, "message": "object deleted"}
