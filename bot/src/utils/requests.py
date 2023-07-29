from random import choice

from core.aio_client import get, post

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


async def get_news():
    try:
        response = await get(
            constants.NEWS_URL.format(settings.NEWS_TOKEN)
        )
    except Exception:
        return constants.API_ERROR
    article = choice(response['articles'])
    return constants.RANDOM_ARTICLE.format(
        article['title'],
        article['url']
    )


async def send_info(message, logger):
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
