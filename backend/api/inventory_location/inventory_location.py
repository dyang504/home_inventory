from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.models import Inventory_location
from .inventory_location_schema import InventoryLocationCreate, InventoryLocationUpdate, InventoryLocationOut
from . import crud_inventory_location
from backend.depedents import (get_current_user, Token, User,
                               authenticate_user, create_access_token,
                               ACCESS_TOKEN_EXPIRE_MINUTES)

router = APIRouter()


@router.get("/inventory_location", response_model=List[InventoryLocationOut])
def read_inventory_location(db: Session = Depends(get_db),
                            current_user: User = Depends(
                                get_current_user)) -> List[Inventory_location]:
    db_obj = crud_inventory_location.inventory_location.get_inventory_location_by_user(
        db=db, user_id=current_user.id)
    return db_obj


@router.post("/inventory_location/create", response_model=InventoryLocationOut)
def create_inventory_location(*,
                              obj_in: InventoryLocationCreate,
                              db: Session = Depends(get_db),
                              current_user: User = Depends(get_current_user)):
    new_obj = crud_inventory_location.inventory_location.create_inventory_location_by_user(
        db=db, obj_in=obj_in, user_id=current_user.id)
    return new_obj


@router.put("/inventory_location/update", response_model=InventoryLocationOut)
def update_inventory_location(*,
                              inventory_location_id: int,
                              obj_in: InventoryLocationUpdate,
                              db: Session = Depends(get_db),
                              current_user: User = Depends(get_current_user)):
    db_obj = crud_inventory_location.inventory_location.get_inventory_location_by_user(
        db=db, user_id=current_user.id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="Inventory location not found")
    if db_obj.user_id != current_user.id:
        raise HTTPException(
            status_code=401,
            detail="Only the owner can modify the inventory location.")
    updated_obj = crud_inventory_location.inventory_location.update(
        db=db, obj_in=obj_in, db_obj=db_obj)
    return updated_obj


@router.delete("/inventory_location/delete")
def delete_inventory_location(*,
                              inventory_location_id: int,
                              db: Session = Depends(get_db),
                              current_user: User = Depends(get_current_user)):
    db_obj = crud_inventory_location.inventory_location.get(
        db=db, id=inventory_location_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="Inventory location not found.")
    if db_obj.user_id != current_user.id:
        raise HTTPException(
            status_code=401,
            detail="Only the owner can delete the inventory location.")
    removed_obj = crud_inventory_location.inventory_location.remove(
        db=db, id=inventory_location_id)
    return {
        "code": 204,
        "message": "object deleted",
        "removed object": removed_obj
    }
