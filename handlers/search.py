from aiogram import Bot
from aiogram.types import Message

from models import db, User
from utils.data import DBInterface


async def start_search(message: Message):
    current_user = DBInterface.get_user_by_id(message.from_user.id)
    active_user = User.query.filter_by(in_search=True).first()
    if active_user:
        active_user.in_search = False
        current_user.in_chat_with = active_user.user_id
        active_user.in_chat_with = current_user.user_id
        db.session.commit()
        await message.answer(f'Congrats, you in chat with {active_user.mention}!')
        await Bot.get_current().send_message(active_user.user_id, f'Congrats, you in chat with {current_user.mention}!')
        return

    current_user.in_search = True
    db.session.commit()
    await message.answer('Please, wait...')


async def stop_search(message: Message):
    user = DBInterface.get_user_by_id(message.from_user.id)
    user.in_search = False
    db.session.commit()
    await message.answer('Search is stopped')


async def stop_chat(message: Message):
    current_user = DBInterface.get_user_by_id(message.from_user.id)
    user_in_chat = DBInterface.get_user_by_id(current_user.in_chat_with)
    current_user.in_chat_with = None
    user_in_chat.in_chat_with = None
    db.session.commit()
    await message.answer('Chat is stopped')
    await Bot.get_current().send_message(user_in_chat.user_id, 'Chat is stopped')

