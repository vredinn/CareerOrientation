import config
import aiogram
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token=config.TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветик!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Закрытие')
        