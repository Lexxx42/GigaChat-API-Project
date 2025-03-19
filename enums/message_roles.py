"""Message roles."""

from enum import StrEnum, auto


class MessageRoles(StrEnum):
    """Message roles."""

    # контекст
    SYSTEM = auto()
    # запрос пользователя
    USER = auto()
    # ответ модели
    ASSISTANT = auto()
