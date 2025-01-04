from aiogram import Router, types
from btn import create_keyboard
from aiogram.filters import Command
from answer import load_data_json, search_in_data_json, format_response
from gpt_bot import get_openai_response


router = Router()
data_json = load_data_json()


def get_relevant_context(data, query):
    """
    Находит релевантный контекст для запроса пользователя.
    Args:
        data (dict): База знаний
        query (str): Запрос пользователя
    Returns:
        str: Релевантный контекст для GPT
    """
    max_similarity = 0
    relevant_section = None
    
    for item in data:
        if "text" in item and "content" in item:
            relevance = sum(1 for word in query.split() 
                          if word in item["text"].lower())
            if relevance > max_similarity:
                max_similarity = relevance
                relevant_section = item

    if relevant_section:
        return f"**{relevant_section['text']}**\n" + "\n".join(relevant_section['content'])
    return "Основная информация о LATOKEN и блокчейн-технологиях"


@router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение и клавиатуру с кнопками.
    """
    photo_url = "https://i.ibb.co/GM8fYn2/1-nkw-Ov-Y7-FSKx-Gt1-ww-W0-DEA.png"
    keyboard = create_keyboard() 
    await message.answer_photo(photo_url, caption="Привет! Я бот LATOKEN. И я расскажу тебе о нашей компании и отвечу на все твои вопросы!", reply_markup=keyboard)


@router.message()
async def handle_message(message: types.Message):
    """
    Обработчик текстовых сообщений.
    Ищет ответ в базе знаний или генерирует его с помощью GPT.
    """
    query = message.text.lower()
    deck_response = search_in_data_json(data_json, query)
    
    if deck_response:
        await message.answer(deck_response, parse_mode="Markdown")
        return
    
    loading_msg = await message.answer("🔄 Анализирую ваш вопрос...")
    context = get_relevant_context(data_json, query)
    gpt_response = await get_openai_response(query, context)
    await loading_msg.edit_text(gpt_response)
