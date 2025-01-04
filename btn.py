from aiogram import Router
from aiogram.types import Message, CallbackQuery
from answer import search_in_data_json, load_data_json

data_json = load_data_json()
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
    context = "LATOKEN — это ведущая криптовалютная биржа, которая специализируется на токенезации и торговле активами. Она обеспечивает удобные, безопасные и доступные услуги для покупки, продажи, обмена и хранения широкого спектра криптовалют и токенов."
    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", url="https://coda.io/@latoken/latoken-talent/latoken-161")]
    ]

    await callback_query.message.answer_photo(photo_url, caption=context, reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))
    await callback_query.answer() 


@buttons_router.callback_query(lambda c: c.data == "btn_hackathon")
async def btn2_handler(callback_query: CallbackQuery):
    
    photo_url ="https://i.ibb.co/dfvxsxp/image.png"
    context = "Хакатон - это мероприятие, которое обычно длится несколько дней, где программисты, дизайнеры, менеджеры продуктов и другие специалисты в сфере IT собираются вместе для создания рабочего прототипа программного обеспечения или аппаратного обеспечения. Цель хакатона - командно и в сжатые сроки разработать инновационное технологическое решение для какой-либо проблемы.\n\nВ контексте LATOKEN и блокчейн технологии, хакатон может быть направлен на создание новых криптовалют, децентрализованных приложений, смарт-контрактов и других решений, использующих технологию блокчейна. Этот процесс позволяет быстро внести инновации в экосистему, тестируя новые идеи и пути развития технологии."

    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", url="https://deliver.latoken.com/hackathon")]
    ]

    await callback_query.message.answer_photo(photo_url, caption=context, reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))
    await callback_query.answer()