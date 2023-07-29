from aiogram import types

from main import dp
from core.aio_client import get
from core.exceptions import WeatherApiException
from utils.get_weather import get_weather

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer('hi, achiva')


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


@dp.message_handler(commands='weather')
async def send_weather(message: types.Message):
    args = message.get_args()  # Получить аргументы команды
    if args:
        city = args.strip()  # Удалить пробелы по краям строки
        # Тут код для получения погоды в городе city
        # Например:
        weather_info = await get_weather(city)  # Предполагаем, что это ваша функция для запроса погоды
        await message.answer(weather_info)
    else:
        await message.answer('Пожалуйста, введите название города. Например: /weather Москва')
