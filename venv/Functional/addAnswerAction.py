from aiogram.utils.chat_action import ChatActionSender
import asyncio

class ContinuousChatAction:
    def __init__(self, bot, chat_id, action, interval=3):
        self.bot = bot
        self.chat_id = chat_id
        self.action = action
        self.interval = interval
        self.task = None

    async def __aenter__(self):
        print(f"Starting {self.action} action")
        self.task = asyncio.create_task(self._send_chat_action())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        print(f"Ending {self.action} action")

    async def _send_chat_action(self):
        while True:
            await self.bot.send_chat_action(chat_id=self.chat_id, action=self.action)
            await asyncio.sleep(self.interval)