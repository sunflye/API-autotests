from pydantic import BaseModel
from typing import List

class AdditionRequest(BaseModel):
    """
    Модель запроса для вложенного объекта addition.
    """
    additional_info: str
    additional_number: int

class AdditionResponse(AdditionRequest):
    """
    Модель ответа для вложенного объекта addition.
    """
    id: int

class EntityRequest(BaseModel):
    """
    Модель запроса для основной сущности.
    """
    addition: AdditionRequest
    important_numbers: List[int]
    title: str
    verified: bool

class EntityResponse(EntityRequest):
    """
    Модель ответа для основной сущности.
    """
    id: int
    addition: AdditionResponse