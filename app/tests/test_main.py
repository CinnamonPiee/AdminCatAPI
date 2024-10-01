import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.main import app
from app.core.models.base import Base
from app.core.models.db_helper import db_helper
from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.test_db_url
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                             "check_same_thread": False})


TestingSessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


@pytest.fixture(scope="module", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="module")
async def async_db_session():
    async with TestingSessionLocal() as session:
        yield session


@pytest.fixture(scope="module")
async def async_client():
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[db_helper.session_dependency()] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
