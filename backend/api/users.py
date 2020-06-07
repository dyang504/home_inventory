from typing import List

from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db import models
from backend.crud import crud_user
from backend.schema.user_schema import UserCreate, UserUpdate, UserOut

router = APIRouter()


@router.get("/user/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@router.get("/user/", response_model=List[UserOut])
def read_all_user(db: Session = Depends(get_db)):
    db_users = crud_user.user.get_all_user(db=db)
    if db_users is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_users


@router.post("/user/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(
        models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400,
                            detail="Email already registered.")

    new_user = crud_user.user.create(db=db, obj_in=user)

    return new_user


@router.put("/user/update", response_model=UserOut)
def update_user(user_id: int,
                obj_in: UserUpdate,
                db: Session = Depends(get_db)):
    updated_user = crud_user.user.update(user_id=user_id, db=db, obj_in=obj_in)
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=200, detail="User not found.")


@router.delete("/user/delete", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    removed_user = crud_user.item.remove(db=db, id=user_id)
    if removed_user:
        return {"code": 200, "message": "User removed."}
    else:
        HTTPException(status_code=404, detail="User not found.")
