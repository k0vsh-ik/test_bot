import random

from aiogram import types
from aiogram.dispatcher.filters import Command

from states import Questions
from loader import dp, country

random.shuffle(country)


@dp.message_handler(Command("game"))
async def gameStart(msg: types.Message):
    await msg.answer("Игра начинается...")
    await msg.answer(f"Назовите столицу -> {country[0]}")
    await Questions.first()


