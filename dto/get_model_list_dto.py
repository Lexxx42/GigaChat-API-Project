"""Response schema: GET /models."""

from pydantic import Field, StrictStr

from dto.generic import GigaChatBaseModel
from dto.models_data_dto import ModelsDataDto


class GetModelListDto(GigaChatBaseModel):
    """Schema for GET /models response."""

    object: StrictStr = Field(description="Тип сущности в ответе, например, список.")
    data: list[ModelsDataDto]
