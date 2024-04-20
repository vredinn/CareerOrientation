from aiogram import F, Router, Bot
from aiogram.client import bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
import app.keyboards as kb
from handlers import get_start
import database

router = Router()

#Состояния удаления
class DeleteState(StatesGroup):
    delete_comfirmation = State()
    

#Удаление аккаунта
@router.callback_query(F.data == 'delete_account')
async def delete_account(callback: CallbackQuery, state: FSMContext): 
    await callback.message.edit_text('Вы действительно хотите удалить данные о себе?',
                                     reply_markup=kb.delete)    
    await state.set_state(DeleteState.delete_comfirmation)
    await callback.answer('')

#подтверждение удаления
@router.callback_query(DeleteState.delete_comfirmation, F.data == 'Yes')
async def confirm_delete(callback: CallbackQuery, state: FSMContext): 
    db = database.Database('dbbot.db')
    users = db.select_user(callback.from_user.id)
    db.delete_user(callback.from_user.id)
    await callback.answer('')
    await callback.message.edit_text('Данные о пользователе удалены')
    await callback.message.answer('👋Привет! \
                                     \n🤖Я Профориентатор,Ваш виртуалный помошник в выборе будующей профессии. \
                                     \n⚡️Для начала необходимо пройти небольшую регистрацию.',
                                     reply_markup=kb.start_unreg)
    await state.clear()

#отмена удаления
@router.callback_query(DeleteState.delete_comfirmation, F.data == 'No')
async def cancel_delete(callback: CallbackQuery, state: FSMContext):
    db = database.Database('dbbot.db')
    users = db.select_user(callback.from_user.id)
    await callback.message.edit_text(f'{users[1]}\nЗдравствуй',
                            reply_markup=kb.start_reg)  
    await callback.answer('')
    await state.clear()    
