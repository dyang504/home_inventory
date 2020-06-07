from pydantic import BaseModel


class NutritionBase(BaseModel):
    name: str
    value: float
    unit: str

    class Config:
        orm_mode = True


class NutritionCreate(NutritionBase):
    pass


class NutritionUpdate(NutritionBase):
    pass


class NutritionOut(NutritionBase):
    pass