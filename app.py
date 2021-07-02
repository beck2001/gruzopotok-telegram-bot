from aiogram import executor, Dispatcher

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher: Dispatcher):
    # set default bot commands
    await set_default_commands(dispatcher)

    # notify admins about bot start
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(skip_updates=True, dispatcher=dp, on_startup=on_startup)
