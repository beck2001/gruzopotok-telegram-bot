from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsAdmin
from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(IsAdmin(), Command("ban"))
async def ban_user(message: types.Message, state: FSMContext):
    await message.answer(f"Введите id пользователя")
    await state.set_state("user_id")


@dp.message_handler(state="user_id")
async def ban_user_id(message: types.Message, state: FSMContext):
    telegram_id = message.text
    await sql_commands.add_banned_user(id=telegram_id)
    await message.answer(f"Пользователь заблокирован")
    await state.finish()
