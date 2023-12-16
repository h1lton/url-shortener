from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.shortener.exceptions import PathNotUniqueException
from starlette import status

from src.shortener.models import LinkModel


async def get_link(session: AsyncSession, path: str) -> Optional[LinkModel]:
    return await session.get(LinkModel, path)


async def create_link(
    session: AsyncSession, link: str, path: Optional[str] = None
) -> LinkModel:
    if path:
        model = LinkModel(path=path, link=link)
    else:
        model = LinkModel(link=link)
    session.add(model)
    try:
        await session.commit()
    except IntegrityError as err:
        await session.rollback()
        if 1062 == err.orig.args[0]:
            if not path:
                model = await create_link(session, link)
            else:
                raise PathNotUniqueException
        else:
            raise err
    return model
