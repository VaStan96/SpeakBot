from settings import bot, Secret


async def start_bot():
    await bot.send_message(Secret.admin_id, 'Start BOT')


async def stop_bot():
    await bot.send_message(Secret.admin_id, 'Stop BOT')