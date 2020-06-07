from sqlalchemy.orm import Session

from backend.crud.base import CRUDBase
from backend.db.models import Size
from backend.schema.size_schema import SizeCreate, SizeUpdate


class CRUDSize(CRUDBase[Size, SizeCreate, SizeUpdate]):
    pass


size = CRUDSize(Size)
