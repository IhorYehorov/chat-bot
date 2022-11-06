from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from utils.data import DBInterface


async def start(message: Message, state: FSMContext):
    if not DBInterface.get_user_by_id(message.from_user.id):
        DBInterface.create_user(message.from_user)

    await state.finish()
    await message.answer('Hello, lets make a party!')
