from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api import sql_commands


class ACLMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User):
        user_id = user.id
        await sql_commands.add_user(id=user_id, name=user.full_name)

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user)

    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, callback_query.from_user)
