from typing import List, Optional
from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db import models

from backend.schema.item_schema import ItemBase, ItemCreate, ItemOut, ItemCreateAll, ItemUpdate
from backend.crud import crud_item

router = APIRouter()


@router.get('/itemlist', response_model=List[ItemOut])
def read_itemlist(user_id: int, db: Session = Depends(get_db)):
    new_items = crud_item.item.get_all_items(db=db, user_id=user_id)
    return new_items


@router.get('/item', response_model=ItemOut)
def read_item(
    id: int, user_id: int, db: Session = Depends(get_db)) -> Optional[ItemOut]:
    db_obj = crud_item.item.get(db=db, id=id)
    return db_obj


@router.post('/item/create', response_model=ItemOut)
def create_item(item: ItemCreate, user_id: int, db: Session = Depends(get_db)):
    new_item = crud_item.item.create_with_owner(db=db,
                                                obj_in=item,
                                                owner_id=user_id)
    return new_item


@router.post('/full_item/create', response_model=ItemOut)
def create_full_item(item: ItemCreateAll,
                     user_id: int,
                     db: Session = Depends(get_db)):
    new_item = crud_item.item.create_full_record(db=db,
                                                 obj_in=item,
                                                 owner_id=user_id)
    return new_item


@router.put('/item/update', response_model=ItemOut)
def update_item(*,
                user_id: int,
                item_id: int,
                obj_in: ItemUpdate,
                db: Session = Depends(get_db)):
    db_obj = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_obj:
        updated_obj = crud_item.item.update(db=db,
                                            db_obj=db_obj,
                                            obj_in=obj_in)
        return updated_obj
    else:
        raise HTTPException(status_code=404, detail="Item not found.")


@router.delete('/item/delete', response_model=ItemOut)
def delete_item(*, item_id: int, db: Session = Depends(get_db)):
    removed_obj = crud_item.item.remove(db=db, id=item_id)
    if removed_obj:
        return {"code": 204, "message": "object deleted"}
