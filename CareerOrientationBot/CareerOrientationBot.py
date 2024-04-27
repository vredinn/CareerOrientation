import config
import logging
from app.loader import loop
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from handlers import get_start, registration, delete_account, test

bot = Bot(token=config.TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()
   
async def main():
    dp.include_router(get_start.router)
    dp.include_router(registration.router)    
    dp.include_router(delete_account.router)
    dp.include_router(test.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Закрытие')