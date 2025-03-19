"""Request schema for count tokens in request: POST /tokens/count."""

from pydantic import Field, StrictStr

from dto.generic import GigaChatBaseModel
from enums.model_ids import ModelIds


class PostTokenCountRequestDto(GigaChatBaseModel):
    """Request schema for count tokens in request: POST /tokens/count."""

    model: ModelIds = Field(description="Название модели, которая будет использована для подсчета количества токенов.")
    input: StrictStr | list[StrictStr] = Field(
        description="Строка или массив строк, в которых надо подсчитать количество токенов.",
    )
