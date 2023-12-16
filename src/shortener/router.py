from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.shortener.schemas import (
    GetLinkScheme,
    LinkObjectJSONAPIScheme,
    CreateLinkScheme,
)
from .exceptions import PathNotUniqueException
from .service import create_link as _create_link, get_link as _get_link
from ..config import settings
from ..database import get_async_session

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_link(
    params: CreateLinkScheme,
    request: Request,
    session: AsyncSession = Depends(get_async_session),
) -> LinkObjectJSONAPIScheme:
    if params.path in settings.LIST_OF_DENIED_PATHS:
        raise PathNotUniqueException

    link_model = await _create_link(session, params.link, params.path)

    return LinkObjectJSONAPIScheme(
        attributes=link_model,
        links={"self": str(request.base_url) + link_model.path},
    )


@router.get("/{path}", response_class=RedirectResponse)
async def get_link(path: str, session: AsyncSession = Depends(get_async_session)):
    try:
        GetLinkScheme(path=path)
    except ValidationError as err:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=err.json()
        )

    object_link = await _get_link(session, path)

    if object_link:
        return object_link.link
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
