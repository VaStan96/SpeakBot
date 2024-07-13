from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, add_user, change_element, get_element
from States import BotState
from Functional import toAI
import Keyboards
import lang_dict

router = Router()


@router.message(BotState.Feedback, F.text.in_(lang_dict.LangDict["GetFeedbackYesBut"]))
async def start_feedback(message: Message, state: FSMContext):

    chatID = get_element.get_chatID(message.from_user.id)
    text = lang_dict.LangDict["PostFeedback"][get_element.get_natLangID(message.from_user.id)]

    answer = toAI.request_to_AI(text, chatID)
    await message.answer(answer)

    await message.answer(
        lang_dict.LangDict["StartDialogText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.go_train(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.ReadyForDialog)


@router.message(BotState.Feedback, F.text.in_(lang_dict.LangDict["GetFeedbackNoBut"]))
async def stop_feedback(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.LangDict["StartDialogText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.go_train(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.ReadyForDialog)



@router.message(BotState.Feedback)
async def catch_text(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageFormatText"][get_element.get_natLangID(message.from_user.id)])