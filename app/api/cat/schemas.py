from pydantic import BaseModel, ConfigDict


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
    model_config = ConfigDict(from_attributes=True)
