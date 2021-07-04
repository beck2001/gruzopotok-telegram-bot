from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("find"))
async def bot_find(message: types.Message):
    pass
