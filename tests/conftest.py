import os

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.models import get_session


@pytest.fixture
def app_client():
    yield app


@pytest.fixture
def client(app_client):
    with TestClient(app_client) as client:
        yield client


@pytest.fixture()
def session():
    os.system('make migrate')

    yield next(get_session())

    os.system('./bin/dbmate drop')
