from tests.api.models import EntityResponse, EntityRequest


def assert_entity_equal(entity: EntityResponse, expected: EntityRequest):
    assert entity.title == expected.title
    assert entity.important_numbers == expected.important_numbers
    assert entity.verified == expected.verified
    assert entity.addition.additional_info == expected.addition.additional_info
    assert entity.addition.additional_number == expected.addition.additional_number
