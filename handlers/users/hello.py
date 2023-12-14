from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards.default as kb

from loader import dp


@dp.message_handler(text='Привет')
async def bot_hello(message: types.Message):
    await message.answer("Привет", reply_markup=kb.keyboard1.hello_kb)
