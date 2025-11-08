import pytest
from tests.api.api_client import EntityApiClient
from tests.api.data import make_entity_request


@pytest.fixture(scope="session")
def client():
    return EntityApiClient("http://localhost:8080")


@pytest.fixture
def entity_request():
    return make_entity_request()
