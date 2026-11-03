import asyncio
import logging
from aiogram import Bot, Dispatcher

dp = Dispatcher()

async def main():
    bot = Bot()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())