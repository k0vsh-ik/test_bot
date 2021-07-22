from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

country_capitals = {'Германия': 'берлин',
                    'Франция': 'париж',
                    'Испания': 'мадрид',
                    'Нидерланды': 'амстердам',
                    'Бельгия': 'брюссель',
                    'Польша': 'варшава',
                    'Италия': 'рим',
                    'Швейцария': 'берн',
                    'Швеция': 'стокгольм',
                    'Дания': 'копенгаген'}

country = ['Германия',
           'Франция',
           'Испания',
           'Нидерланды',
           'Бельгия',
           'Польша',
           'Италия',
           'Швейцария',
           'Швеция',
           'Дания']

capitals = ['берлин',
            'париж',
            'мадрид',
            'амстердам',
            'брюссель',
            'варшава',
            'рим',
            'берн',
            'стокгольм',
            'копенгаген']
