from aiogram import types

from main import dp
from utils.get_weather import get_weather
from . import constants


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer('hi, achiva')


@dp.message_handler(commands='weather')
async def send_weather(message: types.Message):
    args = message.get_args()
    if args:
        city = args.strip()
        weather_info = await get_weather(city)
        await message.answer(weather_info)
    else:
        await message.answer(constants.FAQ_WEATHER)
