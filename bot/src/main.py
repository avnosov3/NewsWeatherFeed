from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from core.config import settings


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from aiogram import executor
    from handlers.messages import * # noqa
    executor.start_polling(dp)
