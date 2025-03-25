from langchain_core.messages import HumanMessage, SystemMessage

from giga_chat.giga_chat_init import giga_chat

messages = [
    SystemMessage(
        content="Ты эхо-бот, который отвечает пользователю его же сообщением. Пример: "
        "1. Пользователь: [TEXT] Ты: [TEXT]"
        "2. Пользователь: привет, как дила? Ты: привет, как дила?"
        "3. Пользователь: сколько будет 2 + 2? Ты: сколько будет 2 + 2?",
    ),
    HumanMessage(content="[TEXT]: не подскажете ли вы, сударь, сколько времени будет в Москве?"),
]

#print(giga_chat(messages=messages).content)
res = giga_chat.invoke(messages)
print(res.content)
