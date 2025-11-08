from tests.api.models import EntityResponse
from tests.api.utils import assert_entity_equal


def test_create_entity(client, entity_request):
    payload = entity_request.model_dump()
    response = client.create_entity(payload)
    entity_id = response.json()
    assert isinstance(entity_id, int)


def test_get_entity_by_id(client, entity_request):
    payload = entity_request.model_dump()
    create_response = client.create_entity(payload)
    entity_id = create_response.json()
    assert isinstance(entity_id, int)

    get_response = client.get_entity(entity_id)
    assert get_response.status_code == 200

    entity = EntityResponse.model_validate(get_response.json())
    assert_entity_equal(entity, entity_request)


def test_get_all_entities(client, entity_request):
    payload = entity_request.model_dump()
    create_response = client.create_entity(payload)
    entity_id = create_response.json()
    assert isinstance(entity_id, int)

    get_all_response = client.get_all_entities()
    assert get_all_response.status_code == 200

    data = get_all_response.json()
    assert isinstance(data, dict)
    assert "entity" in data
    entities = data["entity"]
    assert isinstance(entities, list)
    assert any(EntityResponse.model_validate(e) for e in entities)


def test_patch_entity(client, entity_request):
    payload = entity_request.model_dump()
    create_response = client.create_entity(payload)
    entity_id = create_response.json()
    assert isinstance(entity_id, int)

    get_response = client.get_entity(entity_id)
    entity_data = get_response.json()
    entity_data["title"] = "Обновлённый заголовок"
    entity_data["verified"] = False

    patch_response = client.patch_entity(entity_id, entity_data)
    assert patch_response.status_code == 204

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
    payload = entity_request.model_dump()
    create_response = client.create_entity(payload)
    entity_id = create_response.json()
    assert isinstance(entity_id, int)

    delete_response = client.delete_entity(entity_id)
    assert delete_response.status_code == 204

    get_response = client.get_entity(entity_id)
    assert get_response.status_code in (400, 404, 500)
