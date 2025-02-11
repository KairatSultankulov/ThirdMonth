from aiogram import types, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)


#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user = message.from_user
    # user.first_name - имя пользователя, есть всегда
    # user.last_name - фамилия, может не быть
    # user.username - ник пользователя, может не быть
    # user.id - уникальный идентификатор пользователя, есть всегда в виде числа
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(text='Наш сайт', url='https://geeks.kg'),
            InlineKeyboardButton(text='Наш инстаграм', url='https://geeks.kg'),
            ],
            [
                InlineKeyboardButton(text='О нас', callback_data='aboutus'),
            ],
            [
                InlineKeyboardButton(text='Оставить жалобу', callback_data='complaint')
            ]
        ]
    )
    await message.answer(f'Hello, {user.first_name}', reply_markup=kb)


async def about_us_handler(callback: CallbackQuery):
    # await callback.answer('О нас', show_alert=True)
    await callback.message.answer('О нас')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_callback_query_handler(about_us_handler, lambda c: c.data =='aboutus')