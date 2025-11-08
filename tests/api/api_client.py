import requests


class EntityApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_entity(self, payload):
        return requests.post(f"{self.base_url}/api/create", json=payload)

    def get_entity(self, entity_id):
        return requests.get(f"{self.base_url}/api/get/{entity_id}")

    def get_all_entities(self):
        return requests.post(f"{self.base_url}/api/getAll")

    def patch_entity(self, entity_id, payload):
        return requests.patch(f"{self.base_url}/api/patch/{entity_id}", json=payload)

    def delete_entity(self, entity_id):
        return requests.delete(f"{self.base_url}/api/delete/{entity_id}")
