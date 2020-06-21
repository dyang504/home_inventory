from typing import List, Dict, Union, Optional, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend.crud.base import CRUDBase
from backend.db.models import User
from backend.schema.user_schema import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, None]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_user(self, db: Session) -> List[User]:
        return db.query(self.model).all()

    def get_user(self, username: str, db: Session) -> User:
        
        db_user = db.query(self.model).filter(self.model.username == username)
        if db_user:
            return db_user

    # def update(self, db: Session, *, db_obj: User,
    #            obj_in: Union[UserUpdate, Dict[str, Any]]):
    #     if isinstance(obj_in, dict):
    #         updated_data = obj_in
    #     else:
    #         updated_data = obj_in.dict(exclude_unset=True)
    #     if updated_data["password"]:

    def authenticate(self):
        pass

    def is_activate(self):
        pass

    def is_superuser(self):
        pass


user = CRUDUser(User)
