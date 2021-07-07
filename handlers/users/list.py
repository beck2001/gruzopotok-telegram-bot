from typing import List
import re
import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_datas import remove_callback
from loader import dp
from utils.db_api import sql_commands
from utils.db_api.schemas.search_model import SearchModel


@dp.message_handler(Command("list"))
async def bot_list(message: types.Message):
    logging.info("List command started working")
    search_models: List[SearchModel] = await sql_commands.select_all_search_models(message.from_user.id)
    for search_model in search_models:
        await message.answer(
            f"Параметр поиска со следующими характеристиками:\n"
            f"Точка отправления: {search_model.source}\n"
            f"Пункт назначения: {search_model.destination}\n"
            f"Период доставки: {search_model.time_period}\n"
            f"Тип транспорта: {search_model.car_type}\n"
            f"Объем от {search_model.volume_from} до {search_model.volume_to}\n"
            f"Масса груза от {search_model.weight_from} до {search_model.weight_to}\n",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=f"❌ Удалить этот параметр",
                            callback_data=remove_callback.new(model_type="search model", id=search_model.id)
                        )
                    ]
                ]
            )
        )
    logging.info("Iteration on search models was successful")


@dp.callback_query_handler(remove_callback.filter(model_type="search model"))
async def remove_search_model(callback_query: types.CallbackQuery, callback_data: dict):
    logging.info(f"Removing search model from database {callback_data}")
    await sql_commands.delete_search_model(telegram_id=callback_query.from_user.id, id=int(callback_data["id"]))
    await callback_query.message.answer(
        text=f"Параметр удален"
    )
    logging.info(f"Search model is removed from database")
