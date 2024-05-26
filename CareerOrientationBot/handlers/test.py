import asyncio
from aiogram.exceptions import TelegramBadRequest
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import BufferedInputFile, InputFile, Message, CallbackQuery, callback_query
from aiogram.fsm.state import StatesGroup,State
from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
import json
import app.keyboards as kb
from handlers import get_start
import re
import os
from database.db import Database

router = Router()

#Состояния регистрации
class TestState(StatesGroup):
    testing = State()      #Состояние для тестирования
    scores ={'chel': 0, 'prir': 0, 'tech': 0, 'znak': 0, 'hud': 0}      #Словарь баллов предраспололженности к типам профессии 

#Тестирование
#Начало тестирования
@router.callback_query(F.data == 'start_test')
async def start_test(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    with open('test/questions.json', 'r') as json_file:                                             #Открытие JSON 
        questions_list = json.load(json_file)    
    await state.update_data(questions_count = len(questions_list['questions']))
    await state.update_data(current_question = 0)
    await state.update_data(questions = questions_list['questions'])
    await state.set_state(TestState.testing)
    await callback.message.answer('❓Тест состоит из 20 вопросов \
                                     \n\n📝В каждом вопросе Вам будет предложено выбрать одну из двух видов деятельности, которая вам больше нравится \
                                     \n\n⏳Время прохождения теста ~ 5 минут', reply_markup=kb.start_test)
    await callback.answer('')

#Ответ на вопрос
@router.callback_query(TestState.testing, F.data.startswith('testing_'))
async def answer_question(callback: CallbackQuery, state: FSMContext):
    
    questions_data = await state.get_data() 
    qList = questions_data.get('questions')
    answer = callback.data.split("_")[1]
    db = Database()
    
    #Ответ a
    if answer == 'a':            
            match qList[questions_data.get('current_question')-1]['answers'][0]['score']:
                case 'chel':
                    TestState.scores['chel'] = TestState.scores['chel'] + 1
                case 'hud':
                    TestState.scores['hud'] = TestState.scores['hud'] + 1
                case 'znak':
                    TestState.scores['znak'] = TestState.scores['znak'] + 1
                case 'tech':
                    TestState.scores['tech'] = TestState.scores['tech'] + 1
                case 'prir':
                    TestState.scores['prir'] = TestState.scores['prir'] + 1
                    
    #Ответ b
    if answer == 'b':  
        match qList[questions_data.get('current_question')-1]['answers'][1]['score']:
            case 'chel':
                TestState.scores['chel'] = TestState.scores['chel'] + 1
            case 'hud':
                TestState.scores['hud'] = TestState.scores['hud'] + 1
            case 'znak':
                TestState.scores['znak'] = TestState.scores['znak'] + 1
            case 'tech':
                TestState.scores['tech'] = TestState.scores['tech'] + 1
            case 'prir':
                TestState.scores['prir'] = TestState.scores['prir'] + 1
                
    #Переход к следующему вопросы
    if questions_data.get('current_question') != questions_data.get('questions_count'):   
        await callback.message.edit_text('❔<b>Вопрос ' + str(questions_data.get('current_question') + 1) + 
                                                    ' из ' + str(questions_data.get('questions_count')) +
                                                    '</b>\n\n👉<u>Выберите вид деятельности, который вам больше нравится:</u>\n\n' + qList[questions_data.get('current_question')]['answers'][0]['text'] + '\n\n' +  
                                            qList[questions_data.get('current_question')]['answers'][1]['text'],
                                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='а', callback_data='testing_a')],
            [InlineKeyboardButton(text='б', callback_data='testing_b')],
            [InlineKeyboardButton(text='Отменить тестирование', callback_data='cancel_test')]
        ]))
        
        await state.update_data(current_question = (questions_data.get('current_question') + 1))
        await callback.answer('')
    #Конец тестирования
    else:        
        await callback.message.edit_text('✅<b>Тест пройден</b>', reply_markup=kb.result_test)
        await callback.answer('')

@router.callback_query(TestState.testing, F.data == 'result')
async def result(callback: CallbackQuery, state: FSMContext):
    highest_score = max(TestState.scores.values())    
    db = Database()
    prof_type = list([key for key, val in TestState.scores.items() if val == highest_score])
        
    prof_type_name = list()
    prof_type_code = list()
    for pt in prof_type:
            
        match pt:
            case 'chel': 
                prof_type_name.insert(0,'Человек-человек')
                prof_type_code.insert(0, '1')
            case 'prir':
                prof_type_name.insert(0,'Человек-природа')
                prof_type_code.insert(0, '3')
            case 'znak':
                prof_type_name.insert(0,'Человек-знаковая система')
                prof_type_code.insert(0, '4')
            case 'tech': 
                prof_type_name.insert(0,'Человек-техника')
                prof_type_code.insert(0, '2')
            case 'hud': 
                prof_type_name.insert(0,'Человек-художественный образ')
                prof_type_code.insert(0, '5')
                
    prof_list = list()
    for pn in prof_type_code:
        prof_list.insert(0,await db.select_prof(pn))
    prof_list = [val for val in prof_list if val]
    prof_type_string = ''
    for prof in prof_type_name:
        prof_type_string = prof_type_string + prof + '\n'
#Вывод результатов тестирования
    if not prof_list:
        await callback.message.edit_text(f'''
<u>Ваша предрасполженность к типам професий:</u>
                                         
🧍‍♂️Человек-человек: {TestState.scores['chel']}
🌳Человек-природа: {TestState.scores['prir']}
🔣Человек-знаковая система: {TestState.scores['znak']}
🛠️Человек-техника: {TestState.scores['tech']}
🖼️Человек-художественный образ: {TestState.scores['hud']}

<u>Вы наиболее расположены к типу професии:</u>\n{prof_type_string}
К сожалению для вас нет подходящих профессий, пройдите тест повторно
''', reply_markup=kb.result_show)
    else:
        prof_string = ''
        for prof_cat in prof_list:
            if prof_cat != ():
                for prof in prof_cat:
                    prof_string = prof_string + str(prof[1]) + '\n'

        result_kb_builder = InlineKeyboardBuilder()
        for prof_cat in prof_list:
            if prof_cat != ():
                for prof in prof_cat:
                     result_kb_builder.button(text = prof[1], callback_data='prof_' + str(prof[0]))      
        else:            
            result_kb_builder.attach(InlineKeyboardBuilder.from_markup(kb.result_show))
            result_kb_builder.adjust(1, True)
            await callback.message.edit_text(f'''
✅<b>Тест пройден</b>

<u>Ваша предрасполженность к типам професий:</u>
                                         
🧍‍♂️Человек-человек: {TestState.scores['chel']}
🌳Человек-природа: {TestState.scores['prir']}
🔣Человек-знаковая система: {TestState.scores['znak']}
🛠️Человек-техника: {TestState.scores['tech']}
🖼️Человек-художественный образ: {TestState.scores['hud']}

⭐️<u>Вы наиболее расположены к типу професии:</u>⭐️\n{prof_type_string}
🌟<u>Вам подходят следующие специальности:</u>🌟\n{prof_string}
👇Узнайте о подобранных специальностях подробнее, нажав кнопки внизу👇
''', reply_markup=result_kb_builder.as_markup())    
    TestState.scores = {'chel': 0, 'prir': 0, 'tech': 0, 'znak': 0, 'hud': 0}
    await callback.answer('')
    
 #Отмена тестирования
@router.callback_query(TestState.testing, F.data == 'cancel_test')
async def cancel_test(callback: CallbackQuery, state: FSMContext):
        await callback.message.delete()
        await state.clear()
        await callback.answer('')
        await get_start.startCallback(callback)

#Просмотр професии
@router.callback_query(TestState.testing, F.data.startswith('prof_'))
async def cancel_test(callback: CallbackQuery, state: FSMContext):    
    db = Database()
    await state.update_data(result_message_text = callback.message.text)
    await state.update_data(result_message_keyboard = callback.message.reply_markup)
    prof = await db.select_prof_byId(callback.data.split("_")[1])
    await callback.message.delete()
    await callback.message.answer_photo(photo= BufferedInputFile(prof[0][5], filename="photo.jpg"),
                                        caption=f'<b><u>Специальность: {prof[0][1]}</u></b>\n\n{prof[0][3]}\n\n<a href = "{prof[0][4]}">Узнать подробнее о поступлении на данную специальность</a>',
                                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                                         [InlineKeyboardButton(text='Выбрать',
                                                                                               callback_data=f'choose_prof_{callback.data.split("_")[1]}')],
                                                                                               [InlineKeyboardButton(text='Назад', callback_data='back_to_results')]])
                                        )        
    await callback.answer('')

#Назад к результатам
@router.callback_query(TestState.testing, F.data == 'back_to_results')
async def cancel_test(callback: CallbackQuery, state: FSMContext):
    result_data = await state.get_data()
    await callback.message.delete()
    await callback.message.answer(result_data.get('result_message_text'), reply_markup=result_data.get('result_message_keyboard'))        
    await callback.answer('')

#Выбор профессии
@router.callback_query(TestState.testing, F.data.startswith('choose_prof_'))
async def choose_prof(callback: CallbackQuery, state: FSMContext):
    db = Database()
    await callback.message.delete()
    await db.insert_prof(callback.from_user.id, callback.data.split("_")[2])
    await callback.message.answer('🎉🎊Поздравляем с выбором специальности!🎊🎉', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ура', callback_data='end_test')]]))        
    await callback.answer('')
    
#Завершение тестирования
@router.callback_query(TestState.testing, F.data.startswith('end_test'))
async def choose_prof(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    await callback.answer('')
    await get_start.startCallback(callback)

