from aiogram import Router, types
from btn import create_keyboard
from aiogram.filters import Command
from answer import load_culture_deck, search_in_culture_deck
import json
from gpt_bot import get_openai_response


router = Router()

culture_deck = load_culture_deck("answer.json")


with open('answer.json', 'r', encoding='utf-8') as file:
    content = file.read().replace('export const ANSWERS = ', '').strip(';')
    ANSWERS = json.loads(content)


@router.message(Command("start"))
async def start_command(message: types.Message):
    '''
    Обработчик команды /start.
    '''

    photo_url ="https://i.ibb.co/GM8fYn2/1-nkw-Ov-Y7-FSKx-Gt1-ww-W0-DEA.png"

    keyboard = create_keyboard() 

    await message.answer_photo(photo_url, caption="Привет я текст заглушка!", reply_markup=keyboard)



@router.message()
async def handle_message(message: types.Message):
    query = message.text.lower()

    deck_response = search_in_culture_deck(culture_deck, query)
    if deck_response:
        await message.answer(deck_response, parse_mode="Markdown")
        return
    
    context = "\n\n".join([f"**{item['title']}**\n{item['content']}" for item in culture_deck])
    gpt_response = await get_openai_response(query, context)
    await message.answer(gpt_response)