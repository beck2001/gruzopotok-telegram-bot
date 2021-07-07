import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.sql_commands import select_all_banned_users


class MiddlewareStages(BaseMiddleware):
    # 1 step
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("-------- have update -------")
        logging.info("1. Pre-process update")
        logging.info("next stage is process update")

        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        banned_users = await select_all_banned_users()
        if user in banned_users:
            if update.message:
                await update.message.answer(f"Вы заблокированы системой")
            elif update.callback_query:
                await update.callback_query.answer(f"Вы заблокированы системой")
            raise CancelHandler()

    # 2 step
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info("2. Process update")
        logging.info("next stage is pre-process message")

    # 3 step
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info("3. Pre-process message")
        logging.info("next stage is filters")

    # 4 step - filters should be written in filters package
    # 5 step
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info("5. Process message")
        logging.info("next stage is handlers")

    # 6 step - handlers should be written in handlers package
    # 7 step
    async def on_post_process_message(self, message: types.Message, from_handler: dict, data: dict):
        logging.info("7. Post-process message")
        logging.info("next stage is post-process update")

    # 8 step
    async def on_post_process_update(self, update: types.Update, from_handler: dict, data: dict):
        logging.info("8. Post-process update")
        logging.info("----- update is processed -----------------")

    # for callback_query
    # async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
    #     await callback_query.answer()


