from aiogram.types import Message
from aiogram.utils import executor
from text import TEXT
from bot import bot,dp
import handlers
from keyboards import movie_information







@dp.message_handler(commands='start')
async def start_commands(message:Message):
    await message.answer(TEXT,reply_markup=movie_information())






if __name__ =='__main__':
    executor.start_polling(dp,skip_updates=True)