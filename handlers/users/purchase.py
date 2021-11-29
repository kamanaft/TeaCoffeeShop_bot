import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, tea_keyboard, coffee_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="We have 2 products in offer: tea and coffee. \n"
                              "If you don't need it  - press Cancel",
                         reply_markup=choice)

# Попробуем использовать фильтр от CallbackData
@dp.callback_query_handler(text_contains="tea")
async def buying_tea(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    # Отобразим что у нас лежит в callback_data
    logging.info(f"{callback_data=}")
    await call.message.answer("You have chosen tea. Thank you.",
                              reply_markup=tea_keyboard)


@dp.callback_query_handler(text_contains="coffee")
async def buying_coffee(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("You have chosen coffe. Thank you.",
                              reply_markup=coffee_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением
    await call.answer("You canceled your purchase", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)
