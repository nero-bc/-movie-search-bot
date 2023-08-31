from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



def movie_information():
    keyboard=InlineKeyboardMarkup()
    search=InlineKeyboardButton(text="Поиск фильмов",callback_data="search")
    keyboard.add(search)
    return keyboard
    



