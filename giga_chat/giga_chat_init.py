"""GigaChat setup."""

from langchain_gigachat.chat_models import GigaChat

from enums.model_ids import ModelIds
from secret_reader import AUTH_KEY

giga_chat = GigaChat(credentials=AUTH_KEY, model=ModelIds.GIGACHAT_2, verify_ssl_certs=False)
