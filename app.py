import logging
from aiogram import executor, Dispatcher

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import db_gino


async def on_startup(dispatcher: Dispatcher):
    # create users table in db
    logging.info(f"Connecting to database")
    await db_gino.on_startup(dp)
    logging.info(f"Creating all tables")
    await db.gino.create_all()

    # set default bot commands
    await set_default_commands(dispatcher)

    # need to add connection to database, possible to do before handler in middlewares

    # notify admins about bot start
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(skip_updates=True, dispatcher=dp, on_startup=on_startup)
