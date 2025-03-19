"""Request schema: POST /embeddings."""

from typing import Literal

from pydantic import Field, StrictStr

from dto.generic import GigaChatBaseModel


class PostEmbeddingsRequestDto(GigaChatBaseModel):
    """Request schema: POST /embeddings."""

    model: Literal["Embeddings"] = Field(
        description="Название модели, которая будет использована для создания эмбеддинга.",
    )
    input: StrictStr | list[StrictStr] = Field(
        description="Строка или массив строк, которые будут использованы для генерации эмбеддинга.",
    )
