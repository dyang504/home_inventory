from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.models import Category
from .category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from . import crud_category
from backend.depedents import (get_current_user, Token, User,
                               authenticate_user, create_access_token,
                               ACCESS_TOKEN_EXPIRE_MINUTES)

router = APIRouter()


@router.get('/category', response_model=List[CategoryOut])
def read_categories(db: Session = Depends(get_db),
                    current_user: User = Depends(
                        get_current_user)) -> List[Category]:
    categories = crud_category.category.get_categories_by_user(
        db=db, user_id=current_user.id)
    return categories


@router.post('/category/create', response_model=CategoryOut)
def create_category(
    obj_in: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Category:
    new_obj = crud_category.category.create_category_with_owner(
        db=db, obj_in=obj_in, user_id=current_user.id)
    return new_obj


@router.put('/category/update', response_model=CategoryOut)
def upate_category(
    category_id: int,
    obj_in: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Category:
    db_obj = crud_category.category.get(db=db, id=category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Catrgory not found.")
    if db_obj.user_id != current_user.id:
        raise HTTPException(status_code=401,
                            detail="Only the owner can modify the category.")
    updated_obj = crud_category.category.update(db=db,
                                                db_obj=db_obj,
                                                obj_in=obj_in)
    return updated_obj


@router.delete('/category/delete', response_model=CategoryOut)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Category:
    db_obj = crud_category.category.get(db=db, id=category_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Catrgory not found.")
    if db_obj.user_id != current_user.id:
        raise HTTPException(status_code=401,
                            detail="Only the owner can modify the category.")
    removed_obj = crud_category.category.remove(db_obj)
    return {
        "code": 204,
        "message": "object deleted",
        "removed object": removed_obj
    }
