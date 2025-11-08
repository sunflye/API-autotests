import requests

class EntityApiClient:
    """
    Клиент для взаимодействия с API сущностей.
    Содержит методы для CRUD-операций над сущностями через HTTP-запросы.
    """
    def __init__(self, base_url):
        """
        :param base_url: Базовый URL тестируемого API.
        """
        self.base_url = base_url

    def create_entity(self, payload):
        """
        Создаёт новую сущность.
        :param payload: Данные для создания сущности.
        :return: Response объекта requests.
        """
        return requests.post(f"{self.base_url}/api/create", json=payload)

    def get_entity(self, entity_id):
        """
        Получает сущность по id.
        :param entity_id: Идентификатор сущности.
        :return: Response объекта requests.
        """
        return requests.get(f"{self.base_url}/api/get/{entity_id}")

    def get_all_entities(self):
        """
        Получает список всех сущностей.
        :return: Response объекта requests.
        """
        return requests.post(f"{self.base_url}/api/getAll")

    def patch_entity(self, entity_id, payload):
        """
        Обновляет сущность по id (PATCH).
        :param entity_id: Идентификатор сущности.
        :param payload: Обновлённые данные.
        :return: Response объекта requests.
        """
        return requests.patch(f"{self.base_url}/api/patch/{entity_id}", json=payload)

    def delete_entity(self, entity_id):
        """
        Удаляет сущность по id.
        :param entity_id: Идентификатор сущности.
        :return: Response объекта requests.
        """
        return requests.delete(f"{self.base_url}/api/delete/{entity_id}")