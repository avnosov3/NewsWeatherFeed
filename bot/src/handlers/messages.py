import logging

from aiogram import types

from main import dp
from utils import requests
from . import constants

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await requests.send_commands(message, logger)
    answer = constants.WELCOME_MESSAGE
    await message.answer(answer)
    await requests.send_answer(message, answer, logger)


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    answer = constants.HELP_MESSAGE
    await requests.send_commands(message, logger)
    await message.answer(answer)
    await requests.send_answer(message, answer, logger)


@dp.message_handler(commands='weather')
async def send_weather(message: types.Message):
    await requests.send_commands(message, logger)
    args = message.get_args()
    if args:
        city = args.strip()
        weather_info = await requests.get_weather(city)
        await message.answer(weather_info)
        await requests.send_answer(message, weather_info, logger)
    else:
        answer = constants.FAQ_WEATHER
        await message.answer(answer)
        await requests.send_answer(message, answer, logger)


@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    await requests.send_commands(message, logger)
    news = await requests.get_news()
    await message.answer(news)
    await requests.send_answer(message, news, logger)
