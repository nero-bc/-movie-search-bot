from aiogram import Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN


bot=Bot(TOKEN)
dp=Dispatcher(bot,storage=MemoryStorage())
