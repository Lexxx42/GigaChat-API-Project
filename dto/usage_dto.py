"""Usage object."""

from pydantic import Field, StrictInt

from dto.generic import GigaChatBaseModel


class UsageDto(GigaChatBaseModel):
    """Usage object."""

    prompt_tokens: StrictInt = Field(description="Количество токенов в строке, для которой сгенерирован эмбеддинг.")
