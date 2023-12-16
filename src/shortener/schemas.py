from typing import Optional

from pydantic import BaseModel, HttpUrl, Field

from src.config import settings

field_pattern = r"^[a-zA-Z0-9_-]+$"

field_path = Field(
    min_length=settings.MIN_LENGTH_PATH,
    max_length=settings.MAX_LENGTH_PATH,
    pattern=field_pattern,
    examples=["short-path"],
)


class CreateLinkScheme(BaseModel):
    path: Optional[str] = field_path
    link: HttpUrl


class GetLinkScheme(BaseModel):
    path: str = field_path
