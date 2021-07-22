from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Questions


@dp.message_handler(Command("game"))
async def gameStart(msg: types.Message):
    await msg.reply("Игра начинается...")
    await Questions.first()
    await msg.answer("Первое состояние")