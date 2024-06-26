﻿from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

#Клавиатура для незарегистрированного пользователя
start_unreg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зарегистрироваться', callback_data='registration')]
])

#Клавиатура для зарегистрированного пользователяы
start_reg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти тестирование', callback_data='start_test')],
    [InlineKeyboardButton(text='Удалить данные о пользователе', callback_data='delete_account')]
])

#Клавиатура для удаления аккаунта
delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='deleteYes')], [InlineKeyboardButton(text='Нет', callback_data='deleteNo')]
])

#Клавиатура начала тестирования
start_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Приступить', callback_data='testing_start')], [InlineKeyboardButton(text='Отменить тестирование', callback_data='cancel_test')]
])

#Клавиатура результатов тестирования
result_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ознакомиться с результаты', callback_data='result')], [InlineKeyboardButton(text='Отменить тестирование', callback_data='cancel_test')]
])

#Клавиатура результатов тестирования
result_show = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти тест повторно', callback_data='start_test')], [InlineKeyboardButton(text='Отменить тестирование', callback_data='cancel_test')]
])