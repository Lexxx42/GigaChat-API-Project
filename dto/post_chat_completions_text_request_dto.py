"""Request schema: POST /chat/completions."""

from pydantic import Field, StrictBool, StrictInt

from dto.generic import GigaChatBaseModel
from dto.message_completions_dto import MessageDto
from enums.model_ids import ModelIds


class PostChatCompletionsTextRequestDto(GigaChatBaseModel):
    """Request schema: POST /chat/completions."""

    model: ModelIds = Field(
        default=ModelIds.GIGACHAT,
        description="идентификатор модели, можно указать конкретную или :latest для выбора наиболее актуальной.",
    )
    stream: StrictBool = Field(default=False, description="если true, будут отправляться частичные ответы сообщений.")
    update_interval: StrictInt = Field(
        default=0, description="интервал в секундах, не чаще которого будут присылаться токены в stream режиме",
    )
    messages: list[MessageDto]
