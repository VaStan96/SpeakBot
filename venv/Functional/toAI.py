import cohere
from settings import Secret

async def request_to_AI(text, chat_id):
    co = cohere.Client(Secret.AI_client_id)

    response = co.chat(
        model = "command-r-plus",
        message = text,
        # здесь ИД-чата из БД
        conversation_id = chat_id,
    )

    answer = response.text
    print(answer)###########
    return answer
