import asyncio
import logging

from bot_config import dp
from handlers import start, other_messeges, picture, complaint_dialog


async def main():
    start.register_handlers(dp)
    picture.register_handlers(dp)
    complaint_dialog.register_handlers(dp)

    #обящательно в самом конце
    other_messeges.register_handlers(dp)
    #запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())