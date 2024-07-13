from aiogram import Dispatcher, types, filters, F
from settings import bot
import logging
import asyncio

from Functional.botEvents import start_bot, stop_bot
from Handlers import common, chooseLang, chooseTreinLang, readyDialog, dialog, feedback, different

async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    dp = Dispatcher()

    dp.include_router(common.router)
    dp.include_router(chooseLang.router)
    dp.include_router(chooseTreinLang.router)
    dp.include_router(readyDialog.router)
    dp.include_router(dialog.router)
    dp.include_router(feedback.router)
    dp.include_router(different.router)
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True) # очистка очереди входящих
    
    await dp.start_polling(bot)  # запуск бесконечного бота

if __name__ == "__main__":
    asyncio.run(start())