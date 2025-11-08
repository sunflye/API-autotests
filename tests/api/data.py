from tests.api.models import AdditionRequest, EntityRequest


def make_entity_request(
    title="Заголовок сущности",
    verified=True,
    additional_info="Дополнительные сведения",
    additional_number=123,
    important_numbers=None,
):
    if important_numbers is None:
        important_numbers = [42, 87, 15]
    return EntityRequest(
        addition=AdditionRequest(
            additional_info=additional_info, additional_number=additional_number
        ),
        important_numbers=important_numbers,
        title=title,
        verified=verified,
    )
