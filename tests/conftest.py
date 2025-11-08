import pytest
from tests.api.api_client import EntityApiClient
from tests.api.data import make_entity_request

@pytest.fixture(scope="session")
def client():
    """
    Фикстура для создания клиента API.
    Используется для отправки запросов к тестируемому сервису.
    """
    return EntityApiClient("http://localhost:8080")

@pytest.fixture
def entity_request():
    """
    Фикстура для генерации стандартного объекта запроса сущности.
    Используется в тестах для создания и обновления сущностей.
    """
    return make_entity_request()