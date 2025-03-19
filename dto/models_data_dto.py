"""Data object for GET /models response."""

from pydantic import Field, StrictStr

from dto.generic import GigaChatBaseModel
from enums.model_ids import ModelIds


class ModelsDataDto(GigaChatBaseModel):
    """Data object for GET /models response."""

    id: ModelIds = Field(description="Название модели.")
    object: StrictStr = Field(description="Тип сущности в ответе, например, модель.")
    owned_by: StrictStr = Field(description="Владелец модели.")
    type: StrictStr = Field(description="Тип модели. Значение chat указывает, что модель используется для генерации.")
