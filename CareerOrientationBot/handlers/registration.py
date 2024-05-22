from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, callback_query
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
from handlers import get_start
import re
from database.db import Database

router = Router()

#Состояния регистрации
class RegisterState(StatesGroup):
    user_name = State()
    user_phone = State()

#Регистрация

@router.callback_query(F.data == 'registration')
async def registration_name(callback: CallbackQuery, state: FSMContext): 
    await state.set_state(RegisterState.user_name)
    await callback.answer('')
    msg = await callback.message.edit_text('🪪Укажите Ваше имя, чтобы я знал как мне к Вам обращаться:')
    await state.update_data(message_id = msg.message_id)

#Ввод имени
@router.message(RegisterState.user_name)
async def registration_number(message: Message, state: FSMContext):
    message_data = await state.get_data()
    message_id =  message_data.get('message_id')
    print(message_id)
    await state.update_data(user_name=message.text)
    await state.set_state(RegisterState.user_phone)
    await message.bot.delete_message(message.from_user.id,message_id)
    msg = await message.answer('📞Введите номер телефона в формате +7**********:') 
    await state.update_data(message_id = msg.message_id)

#Ввод телефона и завершение регистрации
@router.message(RegisterState.user_phone)
async def registration_complete(message: Message, state: FSMContext):    
    message_data = await state.get_data()
    message_id =  message_data.get('message_id')
    await message.bot.delete_message(message.from_user.id,message_id)
    if(re.findall('^\+?[7][-\(]?\d{3}\)?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(user_phone=message.text)
        regdata = await state.get_data() 
        reg_name = regdata.get('user_name')
        reg_phone = regdata.get('user_phone')        
        db = Database()
        await db.insert_user(reg_name, reg_phone, message.from_user.id)
        await get_start.start(message)
        await state.clear()
    else:        
        msg = await message.answer('❌Номер указан в неправильном формате (+7**********)')
        await state.update_data(message_id = msg.message_id)
        
