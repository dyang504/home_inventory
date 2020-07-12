from typing import List
# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from backend.lib.crud_base import CRUDBase
from backend.db.models import Category, Item
from .category_schema import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def get_categories_by_user(self, db: Session,
                               user_id: int) -> List[Category]:
        db_obj = db.query(
            self.model).join(Item).filter(Item.user_id == user_id).all()
        return db_obj

    def create_category_with_owner(self, db: Session, obj_in: CategoryCreate,
                                   user_id: int) -> Category:
        new_obj = Category(name=obj_in.name, user_id=user_id)
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)
        return new_obj


category = CRUDCategory(Category)
