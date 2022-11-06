import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

import config
import handlers
from admin.app import app


def on_startup():
    app.app_context().push()
    logging.basicConfig(level=logging.INFO)

    handlers.setup(dp)


if __name__ == '__main__':
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    executor.start_polling(dp, on_startup=on_startup())
