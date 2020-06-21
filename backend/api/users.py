from typing import List, Any
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials

from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db import models
from backend.crud import crud_user
from backend.schema.user_schema import UserCreate, UserUpdate, UserOut
from backend.depedents import (get_current_user, Token, User,
                               authenticate_user, create_access_token,
                               ACCESS_TOKEN_EXPIRE_MINUTES)
router = APIRouter()


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)) -> Any:
    db_user = authenticate_user(db, form_data.username, form_data.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password.",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.username},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/user/{user_id}", response_model=UserOut)
def read_user(current_user: User = Depends(get_current_user),
              db: Session = Depends(get_db)):
    db_user = db.query(
        models.User).filter(models.User.id == current_user.id).first()
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
def update_user(obj_in: UserUpdate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    updated_user = crud_user.user.update(user_id=current_user.id,
                                         db=db,
                                         obj_in=obj_in)
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=200, detail="User not found.")


@router.delete("/user/delete", response_model=UserOut)
def delete_user(db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    removed_user = crud_user.item.remove(db=db, id=current_user.id)
    if removed_user:
        return {"code": 200, "message": "User removed."}
    else:
        HTTPException(status_code=404, detail="User not found.")
