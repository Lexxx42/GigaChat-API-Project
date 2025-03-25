"""Try to use Giga Chat API to generate python classes from Open API spec."""

import json

from langchain_core.messages import HumanMessage, SystemMessage

from giga_chat.giga_chat_init import giga_chat

with open("open_api_sample.json", "r", encoding="utf8") as file:
    api_doc = json.loads(file.read())

    messages = [
        SystemMessage(
            content="Ты python разработчик."
            "Твоя специализация в работе с библиотекой pydantic по документации."
            "Ссылка на документацию pydantic: https://docs.pydantic.dev/2.10/api/base_model/"
            "Ссылка на документацию python: https://www.python.org/downloads/release/python-3110/"
            "На вход ты получаешь [docs] Open API спецификацию."
            "На выходе ты должен предоставить [result] описание классов pydantic для этой спецификации."
            "[result] должен быть представлен в виде кода на языке python 3.11."
            "[result] должен быть подготовлен на основе документации pydantic и спецификации [docs]."
            "[result] должен использовать исключительно строгие проверки типа данных: "
            "StrictStr, StrictInt, StrictFloat, StrictBool и т.д."
            "[result] должен содержать Enum классы для всех перечислений, если они есть в спецификации."
            "в [result] запрещено использовать устаревшие языковые конструкции и импорты из версий python ниже 3.11."
            "все поля классов [result] должны содержать описание Field(description='[some_description]'), "
            "если описание [some_description] присутствует в спецификации [docs]."
            "все поля классов [result] должны содержать значение по умолчанию Field(default='[value]'), "
            "если [value] указано в спецификации [docs] или если поле не является required."
            "в [result] разрешено передавать аргументы только именовано: https://docs.pydantic.dev/dev/api/fields/."
            # "Если поле модели в спецификации явно не указано как required,
            # то его в [result] у этого поля должно быть указано значение по умолчанию, разрешенного типа данных."
            "[result] должен содержать валидацию обязательности заполнения полей модели, если они обязательны."
            "[result] должен содержать модели pydantic 2.10.0 или выше."
            "Ничего не придумывай и не дополняй. Разрешено использовать только описание из [docs].",
        ),
        HumanMessage(content=f"[docs]: {api_doc}"),
    ]

res = giga_chat.invoke(messages)
print(res.content)  # noqa
