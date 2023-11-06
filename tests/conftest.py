from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.models import get_session


def override_get_db():
    try:
        db = MagicMock()
        yield db
    finally:
        db.close()


@pytest.fixture
def app_client():
    yield app


@pytest.fixture
def client(app_client):
    app_client.dependency_overrides[get_session] = override_get_db
    with TestClient(app_client) as client:
        yield client
