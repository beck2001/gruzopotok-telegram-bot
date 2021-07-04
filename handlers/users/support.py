from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("support"))
async def bot_support(message: types.Message):
    pass
