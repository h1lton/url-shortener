import pytest

from httpx import AsyncClient

from starlette import status
from tests.conftest import BaseTest, BASE_URL


class TestShortener(BaseTest):
    @pytest.fixture(autouse=True)
    def _client(self, ac: AsyncClient):
        self.client = ac

    async def test_create_and_get_with_custom_path(self):
        response = await self.request_create(self.params)
        assert response.status_code == status.HTTP_201_CREATED
        expected_data = {
            "type": "link",
            "attributes": self.params,
            "links": {
                "self": f"{BASE_URL}/{self.params['path']}",
            },
        }
        assert response.json() == expected_data

        response = await self.request_get(self.params["path"])
        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
        assert response.next_request.url == self.params["link"]

    async def test_create_and_get_with_auto_path(self):
        response = await self.request_create(
            {"path": None, "link": self.params["link"]}
        )
        assert response.status_code == status.HTTP_201_CREATED

        response_data = response.json()
        path = response_data["attributes"]["path"]

        response = await self.request_get(path)
        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
        assert response.next_request.url == self.params["link"]

    async def test_create_with_a_busy_path(self):
        response = await self.request_create(self.params)
        assert response.status_code == status.HTTP_409_CONFLICT

    async def test_not_found(self):
        response = await self.request_get("non-existent-path")
        assert response.status_code == status.HTTP_404_NOT_FOUND
