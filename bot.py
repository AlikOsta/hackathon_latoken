import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from btn import buttons_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(buttons_router) 
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())