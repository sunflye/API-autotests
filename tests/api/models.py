from pydantic import BaseModel
from typing import List


class AdditionRequest(BaseModel):
    additional_info: str
    additional_number: int


class AdditionResponse(AdditionRequest):
    id: int


class EntityRequest(BaseModel):
    addition: AdditionRequest
    important_numbers: List[int]
    title: str
    verified: bool


class EntityResponse(EntityRequest):
    id: int
    addition: AdditionResponse
