from pydantic import BaseModel


class SizeBase(BaseModel):
    indicator_name: str
    value: float
    unit: str

    class Config:
        orm_mode = True


class SizeCreate(SizeBase):
    pass


class SizeUpdate(SizeBase):
    pass


class SizeOut(SizeBase):
    pass
