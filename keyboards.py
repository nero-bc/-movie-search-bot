from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



def movie_information():
    keyboard=InlineKeyboardMarkup()
    search=InlineKeyboardButton(text="Search Movies",callback_data="search")
    keyboard.add(search)
    return keyboard
    



