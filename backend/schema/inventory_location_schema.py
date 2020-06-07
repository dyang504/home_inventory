from pydantic import BaseModel


class InventoryLocationBase(BaseModel):
    name: str
    description: str
    image_url: str

    class Config:
        orm_mode = True


class InventoryLocationCreate(InventoryLocationBase):
    pass


class InventoryLocationUpdate(InventoryLocationBase):
    pass


class InventoryLocationOut(InventoryLocationBase):
    pass
