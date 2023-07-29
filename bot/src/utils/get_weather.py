from core.aio_client import get

from . import constants
from core.config import settings


async def get_weather(city):
    try:
        response = await get(
            constants.WEATHER_URL.format(city, settings.WEATHER_TOKEN)
        )
    except Exception:
        return constants.API_ERROR
    if response['cod'] == '401':
        return constants.CHECK_API_KEY
    if response['cod'] == '404':
        return constants.CITY_NOT_FOUND.format(city)
    return constants.WEATHER_OUTPUT.format(
        city,
        response['main']['temp'],
        response['main']['feels_like']
    )
