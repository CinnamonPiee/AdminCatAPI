from pydantic import BaseModel


class KittenBase(BaseModel):
    name: str
    color: str
    age: int
    description: str
    breed_id: int


class KittenCreate(KittenBase):
    pass


class KittenUpdate(KittenBase):
    pass


class Kitten(KittenBase):
    id: int

    class Config:
        orm_mode = True
