from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, country_capitals, country, capitals
from states import Questions


ans = []
@dp.message_handler(state=Questions.Q1)
async def ans1(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]:answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[1]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q2)
async def ans2(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[2]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q3)
async def ans3(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[3]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q4)
async def ans4(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[4]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q5)
async def ans5(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[5]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q6)
async def ans6(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[6]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q7)
async def ans7(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[7]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q8)
async def ans8(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[8]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q9)
async def ans9(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"Назовите столицу -> {country[9]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q10)
async def ans10(msg: types.Message, state: FSMContext, p=0):
    answer = msg.text
    async with state.proxy() as data:
        data[country[9]] = answer
    data = await state.get_data()
    for keys in country_capitals:
        if country_capitals[keys] == data[keys]:
            ans[p] = 'Верно'
        else:
            ans[p] = 'Неверно'
        p += 1
    for i in range(10):
        await msg.answer(f"Ответ на вопрос {i + 1} -> {ans[i]}")
    await state.reset_state()
