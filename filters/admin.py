import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data import config


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        logging.info("Admin filter is triggered")
        return message.from_user.id in config.ADMINS
