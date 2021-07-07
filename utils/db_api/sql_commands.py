from typing import Union

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.banned_user import BannedUser
from utils.db_api.schemas.user import User
from utils.db_api.schemas.cargo import Cargo
from utils.db_api.schemas.search_model import SearchModel


# user commands
async def add_user(id: int, name: str, phone_number: str = None, email: str = None):
    try:
        user = User(id=id, name=name, phone_number=phone_number, email=email)
        await user.create()
    except UniqueViolationError as err:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_phone_number(id: int, phone_number: str):
    user = await User.get(id)
    if user:
        await user.update(phone_number=phone_number).apply()


async def update_user_email(id: int, email: str):
    user = await User.get(id)
    if user:
        await user.update(email=email).apply()


async def add_banned_user(id: int, name: str = None, phone_number: str = None, email: str = None):
    try:
        banned_user = BannedUser(id=id, name=name, phone_number=phone_number, email=email)
        await banned_user.create()
    except UniqueViolationError as err:
        pass


async def select_all_banned_users():
    banned_users = await BannedUser.query.gino.all()
    return banned_users


# cargo commands
async def add_cargo(source: str, destination: str, time_period: str, distance: int, car_type: str, weight_from: int,
                    weight_to: int, volume_from: int, volume_to: int, client_name: str, client_phone_number: str,
                    client_email: str, telegram_id: int):
    cargo = Cargo(source=source, destination=destination, time_period=time_period, distance=distance, car_type=car_type,
                  weight_from=weight_from, weight_to=weight_to, volume_from=volume_from, volume_to=volume_to,
                  client_name=client_name, client_phone_number=client_phone_number, client_email=client_email,
                  telegram_id=telegram_id)
    await cargo.create()


async def select_all_cargos(telegram_id: int):
    cargos = Cargo.query.where(Cargo.telegram_id == telegram_id).gino.all()
    return cargos


async def select_cargo(id: int, telegram_id: int):
    cargo = await Cargo.query.where(Cargo.id == id and Cargo.telegram_id == telegram_id).gino.first()
    return cargo


async def count_cargos():
    total = await db.func.count(Cargo.id).gino.scalar()
    return total


# search model commands
async def add_search_model(source: str, destination: str, time_period: str, distance: int, car_type: str,
                           weight_from: int,
                           weight_to: int, volume_from: int, volume_to: int):
    search_model = SearchModel(source=source, destination=destination, time_period=time_period, distance=distance,
                               car_type=car_type,
                               weight_from=weight_from, weight_to=weight_to, volume_from=volume_from,
                               volume_to=volume_to)
    await search_model.create()


async def select_all_search_models(telegram_id: int):
    search_models = await SearchModel.query.where(SearchModel.telegram_id == telegram_id).gino.all()
    return search_models


async def select_search_model(id: int, telegram_id: int):
    search_model = await SearchModel.query.where(SearchModel.id == id and SearchModel.telegram_id == telegram_id).gino.first()
    return search_model


async def delete_search_model(id: int, telegram_id: int):
    await SearchModel.delete.where(SearchModel.id == id and SearchModel.telegram_id == telegram_id).gino.status()


async def count_search_models():
    total = await db.func.count(SearchModel.id).gino.scalar()
    return total

