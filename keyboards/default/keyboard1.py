from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


button_hello = KeyboardButton('Привет 🚒')

hello_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hello)

