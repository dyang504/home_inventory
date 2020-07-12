from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload

from backend.lib.crud_base import CRUDBase
from backend.db.models import Book_property
from backend.schema.book_property_schema import BookPropertyCreate, BookPropertyUpdate


class CRUDBookProperty(CRUDBase[Book_property, BookPropertyCreate,
                                BookPropertyUpdate]):
    def create_with_item(self, db: Session, item_id: int) -> Book_property:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Book_property(**obj_in_data, item_id=item_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


book_property = CRUDBookProperty(Book_property)
