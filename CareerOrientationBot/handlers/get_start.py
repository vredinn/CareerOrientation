from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, callback_query
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import re
import os
import database

router = Router()

#Команда СТАРТ
@router.message(CommandStart())
async def start(message: Message):    
    db =database.Database('dbbot.db')
    users = db.select_user(message.from_user.id)
    
    if(users):#Приветствие для зарегистрированного пользователя
        await message.answer(f'{users[1]}\nЗдравствуй',
                            reply_markup=kb.start_reg)
    else:#Приветствие для незарегистрированного пользователя
        await message.answer('👋Привет! \
                            \n🤖Я Профориентатор,Ваш виртуалный помошник в выборе будующей профессии. \
                            \n⚡️Для начала необходимо пройти небольшую регистрацию.',
                            reply_markup=kb.start_unreg)
