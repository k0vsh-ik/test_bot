from aiogram import types

from loader import dp
from states import Questions


@dp.message_handler(state=Questions.Q1)
async def ans1(msg: types.Message):
    await dp.send_message(msg.from_user.id, "Первое состояние")