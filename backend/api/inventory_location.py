from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.models import Inventory_location
from backend.schema.inventory_location_schema import InventoryLocationCreate, InventoryLocationUpdate, InventoryLocationOut
from backend.crud import crud_inventory_location

router = APIRouter()


@router.get("/inventory_location", response_model=List[InventoryLocationOut])
def read_inventory_location(db: Session = Depends(get_db)):
    db_obj = crud_inventory_location.inventory_location.get_multi(db=db)
    return db_obj


@router.post("/inventory_location/create", response_model=InventoryLocationOut)
def create_inventory_location(*,
                              obj_in: InventoryLocationCreate,
                              db: Session = Depends(get_db)):
    new_obj = crud_inventory_location.inventory_location.create(db=db,
                                                                obj_in=obj_in)
    return new_obj


@router.put("/inventory_location/update", response_model=InventoryLocationOut)
def update_inventory_location(*,
                              inventory_location_id: int,
                              obj_in: InventoryLocationUpdate,
                              db: Session = Depends(get_db)):
    db_obj = db.query(Inventory_location).filter(
        id == inventory_location_id).first()
    updated_obj = crud_inventory_location.inventory_location.update(
        db=db, obj_in=obj_in, db_obj=db_obj)
    return updated_obj


@router.delete("/inventory_location/delete")
def delete_inventory_location(*,
                              inventory_location_id: int,
                              db: Session = Depends(get_db)):
    db_obj = crud_inventory_location.inventory_location.remove(
        db=db, id=inventory_location_id)
    if db_obj:
        return {"code": 204, "message": "object deleted"}