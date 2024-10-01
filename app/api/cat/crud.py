from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.cat import Breed, Kitten
from .schemas import KittenCreate, KittenUpdate


def get_breeds(db: Session):
    return db.query(Breed).all()

# Получение всех котят


def get_kittens(db: Session):
    return db.query(Kitten).all()

# Получение котят определенной породы


def get_kittens_by_breed(db: Session, breed_id: int):
    return db.query(Kitten).filter(Kitten.breed_id == breed_id).all()

# Получение информации о котенке


def get_kitten(db: Session, kitten_id: int):
    return db.query(Kitten).filter(Kitten.id == kitten_id).first()

# Добавление котенка


def create_kitten(db: Session, kitten: KittenCreate):
    db_kitten = Kitten(**kitten.dict())
    db.add(db_kitten)
    db.commit()
    db.refresh(db_kitten)
    return db_kitten

# Обновление информации о котенке


def update_kitten(db: Session, kitten_id: int, kitten: KittenUpdate):
    db_kitten = get_kitten(db, kitten_id)
    if db_kitten:
        for key, value in kitten.dict().items():
            setattr(db_kitten, key, value)
        db.commit()
        db.refresh(db_kitten)
    return db_kitten

# Удаление котенка


def delete_kitten(db: Session, kitten_id: int):
    db_kitten = get_kitten(db, kitten_id)
    if db_kitten:
        db.delete(db_kitten)
        db.commit()
    return db_kitten
