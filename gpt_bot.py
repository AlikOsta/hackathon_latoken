import openai
from config import API_KEY

openai.api_key = API_KEY


async def get_openai_response(prompt, context=None):
    """Отправляет запрос к OpenAI API."""
    messages = [
        {"role": "system", "content": "Ты помощник LATOKEN. Отвечай на вопросы, используя Culture Deck."},
        {"role": "user", "content": f"Контекст: {context if context else 'Нет контекста'}\n\nВопрос: {prompt}"}
    ]
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    return response.choices[0].message["content"]