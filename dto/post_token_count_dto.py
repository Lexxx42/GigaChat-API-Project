"""Response schema for count tokens in request: POST /tokens/count."""

from pydantic import Field, StrictInt, StrictStr

from dto.generic import GigaChatBaseModel


class PostTokenCountDto(GigaChatBaseModel):
    """Response schema for count tokens in request: POST /tokens/count."""

    object: StrictStr = Field(description="Описание того, какая информация содержится в объекте.")
    tokens: StrictInt = Field(description="Количество токенов в соответствующей строке.")
    characters: StrictInt = Field(description="Количество символов в соответствующей строке.")
