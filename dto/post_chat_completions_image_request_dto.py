"""Request schema: POST /chat/completions."""

from pydantic import Field, StrictStr

from dto.post_chat_completions_text_request_dto import PostChatCompletionsTextRequestDto


class PostChatCompletionsImageRequestDto(PostChatCompletionsTextRequestDto):
    """Request schema: POST /chat/completions."""

    function_call: StrictStr = Field(default="auto")
