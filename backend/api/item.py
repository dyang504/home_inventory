from typing import List, Optional, Any
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, APIRouter, status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials
import secrets
from sqlalchemy.orm import Session
from backend.depedents import (get_current_user, Token, User,
                               authenticate_user, create_access_token,
                               ACCESS_TOKEN_EXPIRE_MINUTES)

from backend.db.database import get_db
from backend.db import models

from backend.schema.item_schema import (ItemBase, ItemCreate, ItemOut,
                                        ItemCreateAll, ItemUpdate)
from backend.schema.user_schema import UserOut
from backend.crud import crud_item, crud_user

router = APIRouter()

security = HTTPBasic()


def get_current_user_name(
        credentials: HTTPBasicCredentials = Depends(security),
        db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == credentials.username).first()
    if user:
        correct_username = secrets.compare_digest(credentials.username,
                                                  user.username)
        correct_password = secrets.compare_digest(credentials.password,
                                                  "admin")
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username


@router.get("/users/name")
def read_current_user(username: str = Depends(get_current_user_name)):
    return {"username": username}


@router.get('/itemlist', response_model=List[ItemOut])
def read_itemlist(
        # user_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)) -> Any:
    new_items = crud_item.item.get_all_items(db=db, user_id=current_user.id)
    return new_items


@router.get('/item', response_model=ItemOut)
def read_item(
        *,
        id: int,
        current_user: models.User = Depends(get_current_user),
        db: Session = Depends(get_db),
) -> Optional[ItemOut]:
    db_obj = crud_item.item.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Item not found.")
    if db_obj.user_id == current_user.id:
        return db_obj
    else:
        raise HTTPException(status_code=400,
                            detail="Only the owner can read the item.")


@router.post('/item/create', response_model=ItemOut)
def create_item(item: ItemCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    new_item = crud_item.item.create_with_owner(db=db,
                                                obj_in=item,
                                                owner_id=current_user.id)
    return new_item


@router.post('/full_item/create', response_model=ItemOut)
def create_full_item(item: ItemCreateAll,
                     current_user: models.User = Depends(get_current_user),
                     db: Session = Depends(get_db)):
    new_item = crud_item.item.create_full_record(db=db,
                                                 obj_in=item,
                                                 owner_id=current_user.id)
    return new_item


@router.put('/item/update', response_model=ItemOut)
def update_item(*,
                item_id: int,
                obj_in: ItemUpdate,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_obj = crud_item.item.get(db=db, id=item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Item not found.")
    if db_obj.user_id != current_user.id:
        raise HTTPException(status_code=401, detail="Permission denied.")
    updated_obj = crud_item.item.update(db=db, db_obj=db_obj, obj_in=obj_in)
    return updated_obj


@router.delete('/item/delete', response_model=ItemOut)
def delete_item(*,
                item_id: int,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_obj = crud_item.item.get(db=db, id=item_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Item not found.")
    if db_obj.user_id == current_user.id:
        removed_obj = crud_item.item.remove(db=db, id=item_id)
        return {
            "code": 204,
            "message": "object deleted",
            "object": removed_obj
        }
    else:
        raise HTTPException(status_code=400,
                            detail="Only the owner can read the item.")
