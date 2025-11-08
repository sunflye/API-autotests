import allure
from tests.api.models import EntityResponse
from tests.api.utils import assert_entity_equal

def test_create_entity(client, entity_request):
    """
    Проверяет успешное создание сущности через POST /api/create.
    """
    with allure.step("Формируем payload для создания сущности"):
        payload = entity_request.model_dump()
    with allure.step("Отправляем запрос на создание сущности"):
        response = client.create_entity(payload)
    with allure.step("Проверяем, что возвращён корректный id"):
        entity_id = response.json()
        assert isinstance(entity_id, int)

def test_get_entity_by_id(client, entity_request):
    """
    Проверяет успешное получение сущности по id через GET /api/get/{id}.
    """
    with allure.step("Создаём сущность для теста"):
        payload = entity_request.model_dump()
        create_response = client.create_entity(payload)
        entity_id = create_response.json()
        assert isinstance(entity_id, int)
    with allure.step("Получаем сущность по id"):
        get_response = client.get_entity(entity_id)
        assert get_response.status_code == 200
        entity = EntityResponse.model_validate(get_response.json())
    with allure.step("Проверяем, что данные совпадают с исходными"):
        assert_entity_equal(entity, entity_request)

def test_get_all_entities(client, entity_request):
    """
    Проверяет успешное получение всех сущностей через POST /api/getAll.
    """
    with allure.step("Создаём сущность для теста"):
        payload = entity_request.model_dump()
        create_response = client.create_entity(payload)
        entity_id = create_response.json()
        assert isinstance(entity_id, int)
    with allure.step("Получаем все сущности"):
        get_all_response = client.get_all_entities()
        assert get_all_response.status_code == 200
        data = get_all_response.json()
        assert isinstance(data, dict)
        assert "entity" in data
        entities = data["entity"]
        assert isinstance(entities, list)
    with allure.step("Проверяем, что хотя бы одна сущность валидна"):
        assert any(EntityResponse.model_validate(e) for e in entities)

def test_patch_entity(client, entity_request):
    """
    Проверяет успешное обновление сущности через PATCH /api/patch/{id}.
    """
    with allure.step("Создаём сущность для теста"):
        payload = entity_request.model_dump()
        create_response = client.create_entity(payload)
        entity_id = create_response.json()
        assert isinstance(entity_id, int)
    with allure.step("Обновляем поля title и verified"):
        get_response = client.get_entity(entity_id)
        entity_data = get_response.json()
        entity_data["title"] = "Обновлённый заголовок"
        entity_data["verified"] = False
        patch_response = client.patch_entity(entity_id, entity_data)
        assert patch_response.status_code == 204
    with allure.step("Проверяем, что изменения применились"):
        get_response = client.get_entity(entity_id)
        entity = EntityResponse.model_validate(get_response.json())
        assert entity.title == "Обновлённый заголовок"
        assert entity.verified is False
        assert entity.important_numbers == entity_request.important_numbers
        assert entity.addition.additional_info == entity_request.addition.additional_info
        assert (
            entity.addition.additional_number == entity_request.addition.additional_number
        )

def test_delete_entity(client, entity_request):
    """
    Проверяет успешное удаление сущности через DELETE /api/delete/{id}.
    """
    with allure.step("Создаём сущность для теста"):
        payload = entity_request.model_dump()
        create_response = client.create_entity(payload)
        entity_id = create_response.json()
        assert isinstance(entity_id, int)
    with allure.step("Удаляем сущность"):
        delete_response = client.delete_entity(entity_id)
        assert delete_response.status_code == 204
    with allure.step("Проверяем, что сущность больше не доступна"):
        get_response = client.get_entity(entity_id)
        assert get_response.status_code in (400, 404, 500)