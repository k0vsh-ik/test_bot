import random

from aiogram import types
from aiogram.dispatcher.filters import Command

from states import Questions
from loader import dp, country



@dp.message_handler(Command("game"))
async def gameStart(msg: types.Message):
    await msg.answer("Игра начинается...")
    random.shuffle(country)
    await msg.answer(f"1. Назовите столицу -> {country[0]}")
    await Questions.first()


