import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from utils.db_api import sql_commands
from utils.misc import rate_limit


@rate_limit(limit=5, key="start_command")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await sql_commands.add_user(id=message.from_user.id, name=message.from_user.full_name)
    await message.answer(
        f"Этот бот умеет выполнять следующие <strong>команды:</strong>\n\n"
        "/start - начать работу с ботом\n"
        "/help - получить это сообщение с подсказками\n"
        "/find - ввести параметры и найти груз\n"
        "/list - вывести список отслеживаемых параметров\n"
        "/support - поддержать этот проект финансово\n\n"
        "Команды для управления <em>данными пользователя</em>:\n"
        "/email - обновить email адрес\n"
        "/phone - обновить номер телефона\n\n"
        "Также этот бот работает в <em>инлайн режиме</em>. Для этого в любом чате введите @gruzopotok_bot и выберите "
        "<strong>груз</strong>, которым вы хотите поделиться "
    )
