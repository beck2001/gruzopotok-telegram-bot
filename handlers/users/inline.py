import logging
from typing import List

from aiogram import types

from loader import dp
from utils.db_api import sql_commands
from utils.db_api.schemas.cargo import Cargo


@dp.inline_handler(text="")
async def show_cargos(query: types.InlineQuery):
    cargos: List[Cargo] = await sql_commands.select_all_cargos(telegram_id=query.from_user.id)
    logging.info(f"Cargos data for user with {query.from_user.id} telegram id: {cargos=}")
    # cargo = await sql_commands.select_cargo(id=1, telegram_id=612247020)
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id=f"{cargo.id}",
                title=f"Груз из {cargo.source} в {cargo.destination}",
                input_message_content=types.InputMessageContent(
                    message_text=f"Груз из {cargo.source} в {cargo.destination}:\n"
                    f"Период времени: {cargo.time_period}\n"
                    f"Расстояние: {cargo.distance}\n"
                    f"Тип машины: {cargo.car_type}\n"
                    f"Масса груза - {cargo.weight}, объем - {cargo.volume}\n"
                    f"Контактные данные клиента: {cargo.client_name}, {cargo.client_phone_number}\n"
                    f"Оплата: {cargo.payment}\n"
                )
                # id=cargo.id,
                # title=cargo.source + " " + cargo.destination,
                # input_message_content=types.InputMessageContent(
                #     message_text=f"Груз из {cargo.source} в {cargo.destination}:\n"
                #                  f"Период времени: {cargo.time_period}\n"
                #                  f"Расстояние: {cargo.distance}\n"
                #                  f"Тип машины: {cargo.car_type}\n"
                #                  f"Масса груза - {cargo.weight}, объем - {cargo.volume}\n"
                #                  f"Контактные данные клиента: {cargo.client_name}, {cargo.client_phone_number}\n"
                #                  f"Оплата: {cargo.payment}\n"
                # )
            )
            for cargo in cargos
        ]
    )
