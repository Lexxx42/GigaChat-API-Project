"""Message schema."""

from pydantic import StrictStr

from dto.generic import GigaChatBaseModel
from enums.message_roles import MessageRoles


class MessageDto(GigaChatBaseModel):
    """Message schema."""

    role: MessageRoles
    content: StrictStr
