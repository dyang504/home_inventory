from pydantic import BaseModel


class StatusBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class StatusCreate(StatusBase):
    pass


class StatusUpdate(StatusBase):
    pass


class StatusOut(StatusBase):
    pass