from aiogram import Router, types
from btn import create_keyboard
from aiogram.filters import Command
from answer import load_culture_deck, search_in_culture_deck
import json
from gpt_bot import get_openai_response


router = Router()

culture_deck = load_culture_deck("./pars_web/data.json")

@router.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start."""
    photo_url = "https://i.ibb.co/GM8fYn2/1-nkw-Ov-Y7-FSKx-Gt1-ww-W0-DEA.png"
    await message.answer_photo(photo_url, caption="Привет! Я бот LATOKEN. Задайте мне любой вопрос.")


@router.message()
async def handle_message(message: types.Message):
    """Обрабатывает пользовательские сообщения."""
    query = message.text.lower()

    qa_database = load_qa_database()
    
    deck_response = search_in_culture_deck(culture_deck, query)
    if deck_response:
        await message.answer(deck_response, parse_mode="Markdown")
        return
    
    loading_msg = await message.answer("🔄 Анализирую ваш вопрос...")
    try:
        gpt_response = await get_openai_response(query)
        add_to_qa_database(qa_database, query, gpt_response)
        await loading_msg.edit_text(gpt_response)
    except Exception as e:
        await loading_msg.edit_text("Произошла ошибка при обработке запроса.")
        print(f"Ошибка: {e}")

