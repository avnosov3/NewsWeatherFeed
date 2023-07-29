from aiogram.types import BotCommand

API_ERROR = 'Сервис временно недоступен'
CHECK_API_KEY = 'Проверьте, пожалуйтса, API ключ'
WEATHER_OUTPUT = 'В городе {} сейчас {} градусов, но ощущается как {} градусов'
CITY_NOT_FOUND = 'Город {} не найден'

WEATHER_URL = (
    'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    '&units=metric'
)

RANDOM_ARTICLE = 'Ловите случайную статью "{}". Ссылка {}'

NEWS_URL = (
    'https://newsapi.org/v2/top-headlines?country=ru&apiKey={}'
)

BOT_COMMANDS = [
    BotCommand(command='start', description='Запустить бот'),
    BotCommand(command='help', description='Узнать команды бота'),
    BotCommand(command='weather', description='Узнать погоду'),
    BotCommand(command='news', description='Узнать случайную новость'),
]
