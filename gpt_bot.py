import openai
from config import API_KEY

openai.api_key = API_KEY


def truncate_context(context, max_length=6000):
    """
    Ограничивает длину контекста для GPT.
    Args:
        context (str): Исходный контекст
        max_length (int): Максимальная длина в словах
    Returns:
        str: Обрезанный контекст
    """
    words = context.split()
    return ' '.join(words[:max_length]) if len(words) > max_length else context


async def get_openai_response(query, context):
    """
    Получает ответ от GPT на основе контекста.
    Args:
        query (str): Вопрос пользователя
        context (str): Контекст для ответа
    Returns:
        str: Ответ от GPT
    """
    try:
        truncated_context = truncate_context(context)
        messages = [
            {"role": "system", "content": f"Ты — бот LATOKEN. Используй следующий контекст для ответа:\n\n{truncated_context}"},
            {"role": "user", "content": query}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=1000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {str(e)}"
