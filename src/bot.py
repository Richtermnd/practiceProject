import os

import aiogram
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import common

token = os.environ.get("BOT_TOKEN", "")
if token == "":
    print("no token provided")
    exit(1)

bot = aiogram.Bot(token=token)
dp = aiogram.Dispatcher(storage=MemoryStorage())


async def run():
    dp.include_routers(
        common.router
    )
    await dp.start_polling(bot)
