from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_TEA, URL_COFFEE
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_tea = InlineKeyboardButton(text="Buy tea", callback_data=buy_callback.new(item_name="tea", quantity=1))
choice.insert(buy_tea)

buy_coffee = InlineKeyboardButton(text="Buy coffee", callback_data=buy_callback.new(item_name="coffee", quantity=1))
choice.insert(buy_coffee)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

#Goods keyboards
tea_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Buy here", url=URL_TEA)
    ]
])
coffee_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Buy here", url=URL_COFFEE)
    ]
])