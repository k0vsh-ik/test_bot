from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

country = {'Германия': 'берлин',
           'Франция': 'париж',
           'Испания': 'мадрид',
           'Нидерланды': 'амстердам',
           'Бельгия': 'брюссель',
           'Польша': 'варшава',
           'Италия': 'рим',
           'Швейцария': 'берн',
           'Швеция': 'стокгольм',
           'Дания': 'копенгаген',
           'Чехия': 'прага',
           'Украина': 'киев',
           'Норвегия': 'осло',
           'Греция': 'афины'}