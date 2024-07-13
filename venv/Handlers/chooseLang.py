from aiogram import Router,F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, add_user, change_element, get_element
from States import BotState
import Keyboards
import lang_dict

router = Router()

@router.message(BotState.Start, F.text.in_(lang_dict.LangDict["LangBig"]))
async def set_natLang(message: Message, state: FSMContext):
    if check_user.check_user(message.from_user.id):
        change_element.change_natLang(message)
    else:
        add_user.new_user(message)
    await message.answer(
        lang_dict.LangDict["ChooseTreinLangText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.change_treinLang(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.NatLang)


@router.message(BotState.Start, F.text)
async def catch_text(message: Message):
    await message.answer(lang_dict.FehlerMessageDifferentText)
    
@router.message(BotState.Start)
async def catch_obj(message: Message):
    await message.answer(lang_dict.FehlerMessageDifferentObj)