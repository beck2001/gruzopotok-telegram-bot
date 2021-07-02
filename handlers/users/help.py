from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(
        f"Этот бот умеет выполнять следующие <strong>команды:</strong>\n\n"
        "/start - начать работу с ботом\n"
        "/help - получить это сообщение с подсказками\n"
        "/find - ввести параметры и найти груз\n"
        "/support - поддержать этот проект финансово\n"
        "/list - вывести список отслеживаемых параметров\n\n"
        "Также этот бот работает в <em>инлайн режиме</em>. Для этого в любом чате введите @gruzopotok_bot и выберите "
        "<strong>груз</strong>, которым вы хотите поделиться "
    )