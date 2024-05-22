from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import BufferedInputFile, Message, CallbackQuery, callback_query
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
        if users[4]:
            prof = await db.select_prof_byId(users[4])
            await message.answer_photo(photo= BufferedInputFile(prof[0][5], filename="photo.jpg"), caption = f'⭐️{users[1]}, Вы прошли профориентацию⭐️ \
                                       \n\n⚡️Ваша специальность:⚡️\n{prof[0][1]} \
                                       \n\n<a href = "{prof[0][4]}">Узнать подробнее о поступлении на данную специальность</a> \
                                       \n\n🔄Если вы хотите пройти тестирование повторно, нажмите соответсвующую кнопку под сообщением',
                                       reply_markup=kb.start_reg)
        else:
            await message.answer(f'✅{users[1]}, Вы зарегистрировались\n➡️Для продолжения процесса профориентации необходимо пройти короткое тестирование',
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
        if users[4]:
            prof = await db.select_prof_byId(users[4])
            await callback.bot.send_photo(callback.from_user.id, photo= BufferedInputFile(prof[0][5], filename="photo.jpg"), caption = f'⭐️{users[1]}, Вы прошли профориентацию⭐️ \
                                          \n\n⚡️Ваша специальность:⚡️\n{prof[0][1]} \
                                          \n\n<a href = "{prof[0][4]}">Узнать подробнее о поступлении на данную специальность</a> \
                                          \n\n🔄Если вы хотите пройти тестирование повторно, нажмите соответсвующую кнопку под сообщением',
                                          reply_markup=kb.start_reg)
        else:
            await callback.bot.send_message(callback.from_user.id, f'✅{users[1]}, Вы зарегистрировались,\n➡️Для продолжения процесса профориентации необходимо пройти короткое тестирование',
                            reply_markup=kb.start_reg)
    else:#Приветствие для незарегистрированного пользователя
        await callback.bot.send_message(callback.from_user.id,'👋Привет! \
                            \n🤖Я Профориентатор,Ваш виртуалный помошник в выборе будующей профессии. \
                            \n⚡️Для начала необходимо пройти небольшую регистрацию.',
                            reply_markup=kb.start_unreg)
