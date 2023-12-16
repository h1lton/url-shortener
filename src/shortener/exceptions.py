from fastapi import HTTPException
from starlette import status

PathNotUniqueException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail=f"This path is already taken",
)
