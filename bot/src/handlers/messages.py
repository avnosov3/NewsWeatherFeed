from aiogram import types

from main import dp
from utils import requests
from . import constants


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer(constants.WELCOME_MESSAGE)


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.answer(constants.HELP_MESSAGE)


@dp.message_handler(commands='weather')
async def send_weather(message: types.Message):
    args = message.get_args()
    if args:
        city = args.strip()
        weather_info = await requests.get_weather(city)
        await message.answer(weather_info)
    else:
        await message.answer(constants.FAQ_WEATHER)


@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    await message.answer(
        await requests.get_news()
    )
