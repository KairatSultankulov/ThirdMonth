import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message):
    await message.answer('Hello')

@dp.message_handler()
async def echo_handler(message):
    await message.answer('Привет')

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())