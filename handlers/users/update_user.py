from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode

from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(Command("email"))
async def bot_email(message: types.Message, state: FSMContext):
    await message.answer(f"Отправьте свой email")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await sql_commands.update_user_email(id=message.from_user.id, email=email)
    user = await sql_commands.select_user(id=message.from_user.id)
    if user:
        await message.answer(
            f"Данные обновлены для пользователя:\n" +
            hcode(f"id={user.id}\n"
                  f"имя={user.name}\n"
                  f"телефон={user.phone_number}\n"
                  f"email={user.email}\n"
            )
        )
    await state.finish()


@dp.message_handler(Command("phone"))
async def bot_phone(message: types.Message, state: FSMContext):
    await message.answer(f"Введите свой номер телефона")
    await state.set_state("phone")


@dp.message_handler(state="phone")
async def enter_phone(message: types.Message, state: FSMContext):
    phone_number = message.text
    await sql_commands.update_user_phone_number(id=message.from_user.id, phone_number=phone_number)
    user = await sql_commands.select_user(id=message.from_user.id)
    if user:
        await message.answer(
            f"Данные обновлены для пользователя:\n" +
            hcode(f"id={user.id}\n"
                  f"имя={user.name}\n"
                  f"телефон={user.phone_number}\n"
                  f"email={user.email}\n"
            )
        )
    await state.finish()

