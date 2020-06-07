from sqlalchemy.orm import Session

from backend.crud.base import CRUDBase
from backend.db.models import Nutrition
from backend.schema.nutrition_schema import NutritionCreate, NutritionUpdate


class CRUDNutrition(CRUDBase[Nutrition, NutritionCreate, NutritionUpdate]):
    pass


nutrition = CRUDNutrition(Nutrition)
