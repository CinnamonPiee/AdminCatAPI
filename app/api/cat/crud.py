from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.models import Breed, Kitten
from schemas import KittenCreate, KittenUpdate


async def get_breeds(session: AsyncSession):
    result = await session.execute(select(Breed))
    return result.scalars().all()


async def get_kittens(session: AsyncSession):
    result = await session.execute(select(Kitten))
    return result.scalars().all()


async def get_kittens_by_breed(session: AsyncSession, breed_id: int):
    result = await session.execute(select(Kitten).filter(Kitten.breed_id == breed_id))
    return result.scalars().all()


async def get_kitten(session: AsyncSession, kitten_id: int):
    result = await session.execute(select(Kitten).filter(Kitten.id == kitten_id))
    return result.scalar_one_or_none()


async def create_kitten(session: AsyncSession, kitten: KittenCreate):
    db_kitten = Kitten(**kitten.dict())
    session.add(db_kitten)
    await session.commit()
    await session.refresh(db_kitten)
    return db_kitten


async def update_kitten(session: AsyncSession, kitten_id: int, kitten: KittenUpdate):
    db_kitten = await get_kitten(session, kitten_id)
    if db_kitten:
        for key, value in kitten.dict().items():
            setattr(db_kitten, key, value)
        await session.commit()
        await session.refresh(db_kitten)
    return db_kitten


async def delete_kitten(session: AsyncSession, kitten_id: int):
    db_kitten = await get_kitten(session, kitten_id)
    if db_kitten:
        await session.delete(db_kitten)
        await session.commit()
    return db_kitten
