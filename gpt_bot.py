import openai
from config import API_KEY

openai.api_key = API_KEY


async def get_openai_response(query, context):
    """
    Функция для получения ответа от GPT-4.
    """
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Ты — бот LATOKEN. Используй следующий контекст для ответа:\n\n{context}"},
                {"role": "user", "content": query}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Произошла ошибка при обращении к GPT-4: {e}"
