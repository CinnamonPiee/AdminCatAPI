from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.db_helper import db_helper
from .schemas import KittenUpdate, KittenCreate
from .crud import (
    get_breeds,
    get_kitten,
    get_kittens_by_breed,
    get_kittens,
    create_kitten,
    update_kitten,
    delete_kitten,
)


router = APIRouter(
    tags=["Cats"],
)


@router.get("/breeds/")
async def read_breeds(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await get_breeds(session)


@router.get("/kittens/")
async def read_kittens(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await get_kittens(session)


@router.get("/kittens/{breed_id}")
async def read_kittens_by_breed(
    breed_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await get_kittens_by_breed(session, breed_id)


@router.get("/kitten/{kitten_id}")
async def read_kitten(
    kitten_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    kitten = await get_kitten(session, kitten_id)
    if not kitten:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.post("/kitten/")
async def create_kitten(
    kitten: KittenCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await create_kitten(session, kitten)


@router.put("/kitten/{kitten_id}")
async def update_kitten(
    kitten_id: int,
    kitten: KittenUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_kitten(session, kitten_id, kitten)


@router.delete("/kitten/{kitten_id}")
async def delete_kitten(
    kitten_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await delete_kitten(session, kitten_id)
