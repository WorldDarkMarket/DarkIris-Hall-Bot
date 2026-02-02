import asyncio
import sys

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

from config import TOKEN
from handlers import start, shopping, bank, darkmarket, darklabs


async def main():
    print(f"--- INICIANDO DARK IRIS HALL ---")
    print(f"Python Version: {sys.version}")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start.router,
        shopping.router,
        bank.router,
        darkmarket.router,
        darklabs.router
    )

    print("Iris Hall Bot Online...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
