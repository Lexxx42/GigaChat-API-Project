"""Response schema: POST /files/{file}/delete."""

from pydantic import Field, StrictBool, StrictStr

from dto.generic import GigaChatBaseModel


class PostFileDeleteDto(GigaChatBaseModel):
    """Response schema: POST /files/{file}/delete."""

    id: StrictStr = Field(description="Идентификатор файла.")
    deleted: StrictBool = Field(description="Признак удаления файла.")
