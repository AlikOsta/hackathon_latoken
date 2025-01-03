from aiogram import Router
from aiogram.types import Message, CallbackQuery

buttons_router = Router()

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="О Latoken", callback_data="btn_latoken")],
            [InlineKeyboardButton(text="Что такое Hackathon", callback_data="btn_hackathon")],
        ]
    )

@buttons_router.callback_query(lambda c: c.data == "btn_latoken")
async def btn1_handler(callback_query: CallbackQuery):

    photo_url ="https://i.ibb.co/Tkmj7L7/crypto-managment-latoken.jpg" 

    await callback_query.message.answer_photo(photo_url, caption="Вы нажали на Кнопку 1!")
    await callback_query.answer() 


@buttons_router.callback_query(lambda c: c.data == "btn_hackathon")
async def btn2_handler(callback_query: CallbackQuery):
    
    photo_url ="https://i.ibb.co/dfvxsxp/image.png"

    await callback_query.message.answer_photo(photo_url, caption="Вы нажали на Кнопку 2!")
    await callback_query.answer() 