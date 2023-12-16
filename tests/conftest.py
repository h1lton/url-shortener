import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from sqlalchemy import text, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings
from src.database import metadata, get_async_session, engine
from src.main import app


class BaseTest:
    @pytest.fixture(autouse=True)
    def _client(self, ac: AsyncClient):
        self.client = ac

    async def request_create(self, data: dict):
        return await self.client.post("/", json=data)

    async def request_get(self, path: str):
        return await self.client.get("/" + path)

    params = {
        "path": "test_path",
        "link": "https://github.com/h1lton",
    }


async def create_database():
    async with engine.connect() as conn:
        await conn.execute(
            text(f"CREATE DATABASE IF NOT EXISTS {settings.DB_TEST_NAME}")
        )


asyncio.run(create_database())

test_engine = create_async_engine(
    settings.DB_DSN_TEST,
    echo=settings.DB_ECHO,
    poolclass=NullPool,
)
metadata.bind = test_engine
async_session_maker = async_sessionmaker(test_engine, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


BASE_URL = "http://test"


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        yield ac
