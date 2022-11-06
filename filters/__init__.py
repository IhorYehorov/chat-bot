from aiogram.types import Message

from utils.data import DBInterface


async def user_in_chat_filter(message: Message):
    current_user = DBInterface.get_user_by_id(message.from_user.id)
    return current_user.in_chat_with

