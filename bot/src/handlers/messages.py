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
    try:
        await post(
            settings.DASHBOARD_URL,
            data=dict(
                username=message.from_user.username,
                message=message.text,
                date=message.date.isoformat(),
                chat=message.chat.title
            )
        )
    except Exception as error:
        logger.error(constants.DASHBOARD_ERROR.format(error))
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
