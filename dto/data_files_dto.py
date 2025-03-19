"""Data object for GET /files response."""

from datetime import datetime
from typing import Literal

from pydantic import UUID4, Field, StrictInt, StrictStr

from dto.generic import GigaChatBaseModel


class DataFilesDto(GigaChatBaseModel):
    """Data object for GET /files response."""

    bytes: StrictInt = Field(description="Размер файла в байтах.")
    created_at: datetime = Field(description="Время создания файла в формате unix timestamp.")
    filename: StrictStr = Field(description="Название файла.")
    id: UUID4 = Field(description="Идентификатор файла, который можно использовать при запросах на генерацию.")
    object: StrictStr = Field(description="Тип объекта.")
    purpose: Literal["general"] = Field(
        description="Назначение файлов. "
        "Значение general указывает на то, что файлы могут использоваться для генерации ответа модели.",
    )
    access_policy: Literal["public", "private"] = Field(default="private", description="Доступность файла")
