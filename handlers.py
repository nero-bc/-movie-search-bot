from aiogram.types import Message
from bot import bot,dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from request import *
from text import TEXT_CANCEL
from aiogram import types
from keyboards import  movie_information


class Movie(StatesGroup):
    search=State()
    movie_information=State()
    movie_info=State()




# search commands

@dp.callback_query_handler(lambda c: c.data =="search")
async def to_come(callback_query: types.CallbackQuery):
    await Movie.search.set()
    await bot.send_message(callback_query.from_user.id, "Enter Movie Title:")



@dp.message_handler(commands='cancel',state=Movie.search)
async def cancel_commands(message:Message,state:FSMContext):
    await state.finish()
    await message.answer(TEXT_CANCEL,reply_markup=movie_information())


@dp.message_handler(state=Movie.search)
async def recip(message:Message,state:FSMContext):
    async with state.proxy()as data:
        data["search"]=message.text
    await message.answer(get_movie_url_by_title(data["search"]),reply_markup=movie_information())








    



