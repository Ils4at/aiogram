from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/run')],
    [KeyboardButton(text='/info')],
    [KeyboardButton(text='/buy')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')


