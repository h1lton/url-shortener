from typing import Optional, Annotated

from pydantic import BaseModel, HttpUrl, Field, ConfigDict

from src.config import settings

field_pattern = r"^[a-zA-Z0-9_-]+$"

field_path = Annotated[
    str,
    Field(
        min_length=settings.MIN_LENGTH_PATH,
        max_length=settings.MAX_LENGTH_PATH,
        pattern=field_pattern,
        examples=["short-path"],
    ),
]


class CreateLinkScheme(BaseModel):
    path: Optional[field_path]
    link: HttpUrl


class LinkScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    path: field_path
    link: HttpUrl


class LinksJSONAPIScheme(BaseModel):
    self: HttpUrl


class LinkObjectJSONAPIScheme(BaseModel):
    type: str = "link"
    attributes: LinkScheme
    links: LinksJSONAPIScheme


class GetLinkScheme(BaseModel):
    path: field_path
