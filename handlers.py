from aiogram import Router, types
from btn import create_keyboard
from aiogram.filters import Command
import json


router = Router()


with open('answer.js', 'r', encoding='utf-8') as file:
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
    '''
    Обработчик сообщений от пользователя. 
    '''

    text = message.text.lower()
    for item in ANSWERS:
        keyword, answer = list(item.items())[0]
        if keyword in text:
            await message.answer(answer)
            return
        
    keyboard = create_keyboard() 
    
    photo_url ="https://i.ibb.co/nnRCD5d/image.jpg"

    await message.answer_photo(photo_url, caption="Извините, я не понимаю ваш вопрос. Попробуйте задать его иначе или нажмите необходимую кнопку!", reply_markup=keyboard)
 