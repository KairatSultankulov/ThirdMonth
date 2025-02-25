from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_handler(message):
    text = message.text #текст сообщения
    #await message.answer('I do not understand You')
    await message.reply('I do not understand You.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
