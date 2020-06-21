from typing import List
from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db import models
from backend.db.models import Status
from backend.schema.status_schema import StatusCreate, StatusUpdate, StatusOut
from backend.crud import crud_status
from backend.depedents import (get_current_user, Token, User,
                               authenticate_user, create_access_token,
                               ACCESS_TOKEN_EXPIRE_MINUTES)
router = APIRouter()


@router.get("/status", response_model=List[StatusOut])
def read_status(db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_obj = crud_status.status.get_multi(db=db).filter(
        models.User.id == current_user.id).all()
    return db_obj


@router.post("/status/create", response_model=StatusOut)
def create_status(*,
                  obj_in: StatusCreate,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    new_obj = crud_status.status.create_status_with_owner(
        db=db, obj_in=obj_in, user_id=current_user.id)
    return new_obj


@router.put("/status/update", response_model=StatusOut)
def update_status(
    *,
    status_id: int,
    obj_in: StatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> StatusOut:
    db_obj = crud_status.get(db=db, id=status_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Status not found.")
    if not db_obj.user_id == current_user.id:
        raise HTTPException(status_code=401,
                            detail="Only owner can update status property.")
    else:
        updated_obj = crud_status.status.update(db=db,
                                                obj_in=obj_in,
                                                db_obj=db_obj)
        return updated_obj


@router.delete("/status/delete")
def delete_status(*,
                  status_id: int,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_obj = crud_status.status.get(db=db, id=status_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Status not found.")
    if not db_obj.user_id == current_user.id:
        raise HTTPException(status_code=401,
                            detail="Only the owner of status can delete.")
    else:
        removed_obj = crud_status.status.remove(db=db, id=status_id)
        return {
            "code": 204,
            "message": "object deleted",
            "removed object": removed_obj
        }
