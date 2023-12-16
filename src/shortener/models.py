import string
from random import choices

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.config import settings
from src.database import BaseModel

characters = string.ascii_letters + string.digits


def create_unique_path():
    return "".join(choices(characters, k=settings.STANDARD_LENGTH_PATH))


class LinkModel(BaseModel):
    path: Mapped[str] = mapped_column(
        String(settings.MAX_LENGTH_PATH),
        default=create_unique_path,
        primary_key=True,
    )
    link: Mapped[str] = mapped_column(String(2048))
