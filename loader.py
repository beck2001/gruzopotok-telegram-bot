from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.db_gino import db

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2()
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
