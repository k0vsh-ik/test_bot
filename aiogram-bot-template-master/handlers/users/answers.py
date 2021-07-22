from random import randint

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, country
from states import Questions


@dp.message_handler(state=Questions.Q1)
async def ans1(msg: types.Message, state: FSMContext):
    pass
