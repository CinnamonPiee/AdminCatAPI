from fastapi import APIRouter
from .cat.views import router as cat_router


router = APIRouter()


router.include_router(router=cat_router, prefix="/cats")
