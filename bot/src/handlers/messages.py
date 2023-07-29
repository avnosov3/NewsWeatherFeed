import logging

from aiogram import types

from main import dp
from utils import requests
from . import constants
from core.aio_client import post
from core.config import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await requests.send_info(message, logger)
    await message.answer(constants.WELCOME_MESSAGE)


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await requests.send_info(message, logger)
    await message.answer(constants.HELP_MESSAGE)


@dp.message_handler(commands='weather')
async def send_weather(message: types.Message):
    await requests.send_info(message, logger)
    args = message.get_args()
    if args:
        city = args.strip()
        weather_info = await requests.get_weather(city)
        await message.answer(weather_info)
    else:
        await message.answer(constants.FAQ_WEATHER)


@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    await requests.send_info(message, logger)
    await message.answer(
        await requests.get_news()
    )
