from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("list"))
async def bot_list(message: types.Message):
    pass
