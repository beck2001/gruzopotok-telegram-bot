import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import save_callback
from loader import dp
from states import Cargo
from utils.db_api import sql_commands


@dp.message_handler(Command("find"))
async def bot_find(message: types.Message, state: FSMContext):
    await message.answer(
        f"Отправьте пункт отправления груза"
    )
    await Cargo.source.set()


@dp.message_handler(state=Cargo.source)
async def find_source(message: types.Message, state: FSMContext):
    source = message.text
    await state.update_data(
        {
            "source": source
        }
    )
    await message.answer(f"Отправьте пункт назначения груза")
    await Cargo.destination.set()


@dp.message_handler(state=Cargo.destination)
async def find_destination(message: types.Message, state: FSMContext):
    destination = message.text
    await state.update_data(
        {
            "destination": destination
        }
    )
    await message.answer(f"Отправьте тип машины")
    await Cargo.car_type.set()


@dp.message_handler(state=Cargo.car_type)
async def find_car_type(message: types.Message, state: FSMContext):
    car_type = message.text
    await state.update_data(
        {
            "car_type": car_type
        }
    )
    await message.answer(f"Отправьте вес груза (от скольки тонн)")
    await Cargo.weight_from.set()


@dp.message_handler(state=Cargo.weight_from)
async def find_weight_from(message: types.Message, state: FSMContext):
    weight_from = message.text
    await state.update_data(
        {
            "weight_from": weight_from
        }
    )
    await message.answer(f"Отправьте вес груза (до скольки тонн)")
    await Cargo.weight_to.set()


@dp.message_handler(state=Cargo.weight_to)
async def find_weight_to(message: types.Message, state: FSMContext):
    weight_to = message.text
    await state.update_data(
        {
            "weight_to": weight_to
        }
    )
    await message.answer(f"Отправьте объем груза (от скольки м3)")
    await Cargo.volume_from.set()


@dp.message_handler(state=Cargo.volume_from)
async def find_volume_from(message: types.Message, state: FSMContext):
    volume_from = message.text
    await state.update_data(
        {
            "volume_from": volume_from
        }
    )
    await message.answer(f"Отправьте объем груза (до скольки м3)")
    await Cargo.volume_to.set()


@dp.message_handler(state=Cargo.volume_to)
async def find_volume_to(message: types.Message, state: FSMContext):
    data = await state.get_data()
    source = data.get("source")
    destination = data.get("destination")
    car_type = data.get("car_type")
    weight_from = data.get("weight_from")
    weight_to = data.get("weight_to")
    volume_from = data.get("volume_from")
    volume_to = message.text

    logging.info(f"Search model object is created")

    await message.answer(
        f"Вы ввели следующие <strong>параметры</strong>:\n"
        f"Точка отправления - <em>{source}</em>\n"
        f"Точка назначения - <em>{destination}</em>\n"
        f"Тип машины - <em>{car_type}</em>\n"
        f"Вес груза от {weight_from} тонн до {weight_to} тонн\n"
        f"Объем груза от {volume_from} м3 до {volume_to} м3\n",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"✔ Сохранить параметр поиска",
                        callback_data=save_callback.new(model_type_to_save="search model", source=source,
                                                        destination=destination,
                                                        car_type=car_type, weight_from=weight_from, weight_to=weight_to,
                                                        volume_from=volume_from, volume_to=volume_to)
                    )
                ]
            ]
        )
    )
    await state.finish()


@dp.callback_query_handler(save_callback.filter(model_type_to_save="search model"))
async def add_search_model(callback_query: types.CallbackQuery, callback_data: dict):
    logging.info(f"Adding search model to database")
    await sql_commands.add_search_model(source=callback_data["source"], destination=callback_data["destination"],
                                        car_type=callback_data["car_type"], weight_from=int(callback_data["weight_from"]),
                                        weight_to=int(callback_data["weight_to"]), volume_from=int(callback_data["volume_from"]),
                                        volume_to=int(callback_data["volume_to"]), telegram_id=callback_query.from_user.id)
    await callback_query.answer(
        text=f"Параметр был добавлен",
        show_alert=True,
        cache_time=60
    )
    logging.info(f"Search model was successfully added to database")

