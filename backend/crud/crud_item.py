from typing import List
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload

from backend.crud.base import CRUDBase
from backend.db.models import Item, Item_info, Nutrition, Item_image, Category
from backend.schema.item_schema import ItemCreate, ItemCreateAll, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, None]):
    def get_all_items(self, db: Session, user_id: int) -> List[Item]:
        db_obj = db.query(self.model).options(
            joinedload('infos')).filter(Item.user_id == user_id).all()
        print(db_obj[0].infos)
        return db_obj

    def create_with_owner(self, db: Session, *, obj_in: ItemCreate,
                          owner_id: int) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Item(name=obj_in.name, user_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_full_record(self, db: Session, *, obj_in: ItemCreateAll,
                           owner_id: int) -> Item:
        obj_in_data = obj_in.dict()
        infos = [Item_info(**info) for info in obj_in_data['infos']]
        nutritions = [Nutrition(**item) for item in obj_in_data['nutritions']]
        images = [Item_image(**image) for image in obj_in_data['images']]
        category = [
            Category(**category) for category in obj_in_data['category']
        ]
        db_obj = self.model(name=obj_in.name,
                            category=category,
                            infos=infos,
                            nutritions=nutritions,
                            image=images,
                            user_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_item_with_owner(self, item_id: int, db: Session, *,
                               db_obj: ItemUpdate, obj_in: ItemCreate,
                               owner_id: int) -> Item:
        db_data = jsonable_encoder(obj_in)
        db_obj = db.query(self.model).filter(self.model.id == item_id).first()
        if isinstance(obj_in, dict):
            updated_data = obj_in
        else:
            updated_data = obj_in.dict(exclude_unset=True)
        if db_obj:
            for field in db_data:
                if field in updated_data:
                    setattr(db_obj, field, updated_data[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        else:
            raise HTTPException(status_code=404, detail="Item not found.")


item = CRUDItem(Item)
