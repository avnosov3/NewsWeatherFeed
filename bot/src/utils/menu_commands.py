from aiogram import Dispatcher

from . import constants


async def set_bot_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(commands=constants.BOT_COMMANDS)
