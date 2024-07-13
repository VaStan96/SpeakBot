from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, add_user, change_element, get_element
from States import BotState
import Keyboards
import lang_dict

from settings import bot
from Functional import getData, delTempFiles, addAnswerAction

#
# from aiogram.utils.chat_action import ChatActionSender
import asyncio
#
# class ContinuousChatAction:
#     def __init__(self, bot, chat_id, action, interval=3):
#         self.bot = bot
#         self.chat_id = chat_id
#         self.action = action
#         self.interval = interval
#         self.task = None
#
#     async def __aenter__(self):
#         self.task = asyncio.create_task(self._send_chat_action())
#         return self
#
#     async def __aexit__(self, exc_type, exc, tb):
#         if self.task:
#             self.task.cancel()
#             try:
#                 await self.task
#             except asyncio.CancelledError:
#                 pass
#
#     async def _send_chat_action(self):
#         while True:
#             async with ChatActionSender(action=self.action, bot=self.bot, chat_id=self.chat_id):
#                 await asyncio.sleep(self.interval)


router = Router()


@router.message(BotState.Dialog, F.text.in_(lang_dict.LangDict["EndTreinBut"]))
async def stop_dialog(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.LangDict["GetFeedbackText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.get_feedback(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.Feedback)


@router.message(BotState.Dialog, F.text)
async def text_dialog(message: Message):
    #async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
    async with addAnswerAction.ContinuousChatAction(bot=bot, chat_id=message.chat.id, action="typing"):
        await asyncio.sleep(5)
        answer = await getData.get_text(message)
        await message.answer(answer)


@router.message(BotState.Dialog, F.voice)
async def voice_dialog(message: Message):
    #async with ChatActionSender.record_voice(bot=bot, chat_id=message.chat.id):
    async with addAnswerAction.ContinuousChatAction(bot=bot, chat_id=message.chat.id, action="record_voice"):
        print("Getting voice data")
        answer, path_file = await getData.get_voice(message)
        print("Getting voice data")
        await message.answer_voice(answer)
        print("Voice answer sent")
    delTempFiles.del_audiofiles(path_file)


@router.message(BotState.Dialog)
async def catch_text(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageFormatText"][get_element.get_natLangID(message.from_user.id)])