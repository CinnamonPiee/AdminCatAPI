from fastapi import FastAPI
from .core.models.base import Base
from .core.models.db_helper import db_helper
from contextlib import asynccontextmanager
from .api.cat.views import router as cat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(cat_router)
