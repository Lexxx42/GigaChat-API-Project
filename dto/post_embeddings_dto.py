"""Response schema: POST /embeddings."""

from pydantic import Field, StrictStr

from dto.data_embeddings_dto import DataEmbeddingsDto
from dto.generic import GigaChatBaseModel


class PostEmbeddingsDto(GigaChatBaseModel):
    """Response schema: POST /embeddings."""

    object: StrictStr = Field(description="Формат структуры данных.")
    data: DataEmbeddingsDto
    model: StrictStr = Field(
        default="Embeddings",
        description="Название модели, которая используется для вычисления эмбеддинга.",
    )
