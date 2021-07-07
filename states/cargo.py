from aiogram.dispatcher.filters.state import StatesGroup, State


class Cargo(StatesGroup):
    source = State()
    destination = State()
    car_type = State()
    weight_from = State()
    weight_to = State()
    volume_from = State()
    volume_to = State()
