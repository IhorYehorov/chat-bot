from aiogram import Bot
from aiogram.types import Message

from utils.data import DBInterface


async def resend_message(message: Message):
    current_user = DBInterface.get_user_by_id(message.from_user.id)
    if user_in_chat_id := current_user.in_chat_with:
        if message.photo:  # TODO
            await Bot.get_current().send_photo(user_in_chat_id, message.photo, message.caption)
        elif message.video:
            await Bot.get_current().send_video(user_in_chat_id, message.video, caption=message.caption)
        elif message.document:
            await Bot.get_current().send_document(user_in_chat_id, message.video, caption=message.caption)
        else:
            await Bot.get_current().send_message(user_in_chat_id, message.text)
