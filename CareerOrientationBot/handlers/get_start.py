from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, callback_query
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
from database.db import Database
    
router = Router()

#Команда СТАРТ
@router.message(CommandStart())
async def start(message: Message):
    db = Database()
    users = await db.select_user(message.from_user.id)
    
    if(users):#Приветствие для зарегистрированного пользователя
        await message.answer(f'{users[1]}\nЗдравствуй',
                            reply_markup=kb.start_reg)
    else:#Приветствие для незарегистрированного пользователя
        await message.answer('👋Привет! \
                            \n🤖Я Профориентатор,Ваш виртуалный помошник в выборе будующей профессии. \
                            \n⚡️Для начала необходимо пройти небольшую регистрацию.',
                            reply_markup=kb.start_unreg)

async def startCallback(callback: CallbackQuery):
    db = Database()
    users = await db.select_user(callback.from_user.id)
    
    if(users):#Приветствие для зарегистрированного пользователя
        await callback.bot.send_message(callback.from_user.id, f'{users[1]}\nЗдравствуй',
                            reply_markup=kb.start_reg)
    else:#Приветствие для незарегистрированного пользователя
        await callback.bot.send_message(callback.from_user.id,'👋Привет! \
                            \n🤖Я Профориентатор,Ваш виртуалный помошник в выборе будующей профессии. \
                            \n⚡️Для начала необходимо пройти небольшую регистрацию.',
                            reply_markup=kb.start_unreg)
