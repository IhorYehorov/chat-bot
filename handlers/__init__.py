from aiogram import Dispatcher

from filters import user_in_chat_filter
from handlers.chat import resend_message
from handlers.search import start_search, stop_search, stop_chat
from handlers.user import start


def setup(dp: Dispatcher):
    # search
    dp.register_message_handler(start_search, commands=['search'])
    dp.register_message_handler(stop_search, commands=['stop_search'])
    dp.register_message_handler(stop_chat, user_in_chat_filter, commands=['stop'])

    # chat
    dp.register_message_handler(resend_message, user_in_chat_filter)

    # user
    dp.register_message_handler(start, commands=['start'])
