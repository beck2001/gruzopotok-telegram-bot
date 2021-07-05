from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "начать работу с ботом"),
            types.BotCommand("help", "помощь в работе с ботом"),
            types.BotCommand("find", "найти груз по параметрам"),
            types.BotCommand("list", "вывести список отслеживаемых параметров"),
            types.BotCommand("support", "поддержать проект"),
            types.BotCommand("email", "обновить email адрес"),
            types.BotCommand("phone", "обновить номер телефона")
        ]
    )
