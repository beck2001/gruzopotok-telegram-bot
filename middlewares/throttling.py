import asyncio
from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood_"):
        self.limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return

        dp = Dispatcher.get_current()

        limit = getattr(handler, "throttling_rate_limit", self.limit)
        key_prefix = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")

        try:
            await dp.throttle(key_prefix, rate=limit)
        except Throttled as t:
            await self.target_throttled(target, t, dp, key_prefix)
            raise CancelHandler()

    @staticmethod
    async def target_throttled(target: Union[types.Message, types.CallbackQuery], t: Throttled, dp: Dispatcher, key: str):
        message = target.message if isinstance(target, types.CallbackQuery) else target
        delta = t.rate - t.delta

        if t.exceeded_count == 2:
            await message.answer(f"Слишком частое использование команды")
            return
        elif t.exceeded_count == 3:
            await message.answer(f"Произошла попытка флуда, бот ответит через {delta}")
            return
        await asyncio.sleep(delta)

        thr = await dp.check_key(key)
        if thr.exceeded_count == t.exceeded_count:
            await message.answer(f"Бот снова готов к работе")

    async def on_process_message(self, message: types.Message, data: dict):
        await self.throttle(message)

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        await self.throttle(call)

