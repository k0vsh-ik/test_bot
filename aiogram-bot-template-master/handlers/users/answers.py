from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, country_capitals, country
from states import Questions

ans = [0] * 10


@dp.message_handler(state=Questions.Q1)
async def ans1(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[0]: answer
        }
    )
    await msg.answer(f"2. Назовите столицу -> {country[1]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q2)
async def ans2(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[1]: answer
        }
    )
    await msg.answer(f"3. Назовите столицу -> {country[2]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q3)
async def ans3(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[2]: answer
        }
    )
    await msg.answer(f"4. Назовите столицу -> {country[3]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q4)
async def ans4(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[3]: answer
        }
    )
    await msg.answer(f"5. Назовите столицу -> {country[4]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q5)
async def ans5(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[4]: answer
        }
    )
    await msg.answer(f"6. Назовите столицу -> {country[5]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q6)
async def ans6(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[5]: answer
        }
    )
    await msg.answer(f"7. Назовите столицу -> {country[6]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q7)
async def ans7(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[6]: answer
        }
    )
    await msg.answer(f"8. Назовите столицу -> {country[7]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q8)
async def ans8(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[7]: answer
        }
    )
    await msg.answer(f"9. Назовите столицу -> {country[8]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q9)
async def ans9(msg: types.Message, state: FSMContext):
    answer = msg.text
    await state.update_data(
        {
            country[8]: answer
        }
    )
    await msg.answer(f"10. Назовите столицу -> {country[9]}")
    await Questions.next()


@dp.message_handler(state=Questions.Q10)
async def ans10(msg: types.Message, state: FSMContext, p=0):
    answer = msg.text
    await state.update_data(
        {
            country[9]: answer
        }
    )

    data = await state.get_data()

    for keys in country_capitals:
        print()
        print(country_capitals[keys])
        print(data[keys])

        if str(country_capitals[keys]).lower() == str(data[keys]).lower():
            ans[p] = 'Верно'
            print('+')

        else:
            ans[p] = 'Неверно'
            print('-')

        p += 1

    for i in range(10):
        await msg.answer(f"Ответ на вопрос {i + 1} -> {ans[i]}")
<<<<<<< Updated upstream

    await state.finish()
=======
    await state.reset_state()
>>>>>>> Stashed changes
