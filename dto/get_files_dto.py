"""Response schema: GET /files."""

from dto.data_files_dto import DataFilesDto
from dto.generic import GigaChatBaseModel


class GetFilesDto(GigaChatBaseModel):
    """Response schema: GET /files."""

    data: list[DataFilesDto]
