"""Data object for POST /embeddings response."""

from pydantic import Field, StrictFloat, StrictInt, StrictStr

from dto.generic import GigaChatBaseModel
from dto.usage_dto import UsageDto


class DataEmbeddingsDto(GigaChatBaseModel):
    """Data object for POST /embeddings response."""

    object: StrictStr = Field(description="Тип объекта.")
    embedding: list[StrictFloat] = Field(
        description="Массив чисел, представляющих значения эмбеддинга для предоставленного текста.",
    )
    index: StrictInt = Field(description="Индекс соответствующий индексу текста, полученного в массиве input запроса.")
    usage: UsageDto
