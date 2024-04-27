﻿from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
import app.keyboards as kb
from handlers import get_start
from database.db import Database

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
@router.callback_query(DeleteState.delete_comfirmation, F.data.startswith('delete'))
async def confirm_delete(callback: CallbackQuery, state: FSMContext): 
    match callback.data:
        case "deleteYes":
            db = Database()
            try:
                await db.delete_user(callback.from_user.id)
            finally:
                await callback.message.edit_text('Данные о пользователе удалены')
        case "deleteNo":
            await callback.message.edit_text('Удаление данных отменено')
    await get_start.startCallback(callback)
    await callback.answer('')
    await state.clear()    
