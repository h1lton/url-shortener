import pytest

from httpx import AsyncClient
from src.config import settings
from starlette import status
from tests.conftest import BaseTest


class TestPathNaming(BaseTest):
    def params_with_path(self, path):
        return {"path": path, "link": self.params["link"]}

    async def test_min_max_length_path_naming(self):
        pack = [
            [
                "s" * settings.MAX_LENGTH_PATH,
                "s" * (settings.MAX_LENGTH_PATH + 1),
            ],
            [
                "s" * settings.MIN_LENGTH_PATH,
                "s" * (settings.MIN_LENGTH_PATH - 1),
            ],
        ]

        for valid_path, not_valid_path in pack:
            response = await self.request_create(
                self.params_with_path(not_valid_path)
            )  # not valid
            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

            response = await self.request_create(
                self.params_with_path(valid_path)
            )  # valid
            assert response.status_code == status.HTTP_201_CREATED

            response = await self.request_get(valid_path)
            assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    async def test_path_naming(self):
        response = await self.request_create(
            self.params_with_path("фывфыв")
        )  # not valid
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        response = await self.request_get("фывфыв")  # not valid
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        paths = ["asdasd", "ASDDAS", "122131", "Aa1-_", "___", "---"]

        for path in paths:
            response = await self.request_create(self.params_with_path(path))
            assert response.status_code == status.HTTP_201_CREATED

            response = await self.request_get(path)
            assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    async def test_docs(self):
        response = await self.request_create(self.params_with_path("docs"))
        assert response.status_code != status.HTTP_409_CONFLICT
