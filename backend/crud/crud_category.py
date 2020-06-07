from typing import List
# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from backend.crud.base import CRUDBase
from backend.db.models import Category, Item
from backend.schema.category_schema import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def get_categories_by_user(self, db: Session,
                               user_id: int) -> List[Category]:
        db_obj = db.query(
            self.model).join(Item).filter(Item.user_id == user_id).all()
        return db_obj


category = CRUDCategory(Category)
