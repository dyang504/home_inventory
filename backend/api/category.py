from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.models import Category
from backend.schema.category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from backend.crud import crud_category

router = APIRouter()


@router.get('/category', response_model=List[CategoryOut])
def read_categories(
    user_id: int, db: Session = Depends(get_db)) -> List[Category]:
    categories = crud_category.category.get_categories_by_user(db=db,
                                                               user_id=user_id)
    return categories


@router.post('/category/create', response_model=CategoryOut)
def create_category(user_id: int, db: Session = Depends(get_db)) -> Category:
    pass


@router.put('/category/update', response_model=CategoryOut)
def upate_category(user_id: int, db: Session = Depends(get_db)) -> Category:
    pass


@router.delete('/category/delete', response_model=CategoryOut)
def delete_category(user_id: int, db: Session = Depends(get_db)) -> Category:
    pass