from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, add_user, change_element, get_element
from States import BotState
import Keyboards
import lang_dict

router = Router()


@router.message(BotState.NatLang, F.text.in_(lang_dict.LangDict["ChooseTreinLangRusBut"]))
@router.message(BotState.NatLang, F.text.in_(lang_dict.LangDict["ChooseTreinLangEngBut"]))
@router.message(BotState.NatLang, F.text.in_(lang_dict.LangDict["ChooseTreinLangDeuBut"]))
async def set_treinLang(message: Message, state: FSMContext):
    change_element.change_treinLang(message)

    await message.answer(
        lang_dict.LangDict["StartDialogText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.go_train(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.ReadyForDialog)


@router.message(BotState.NatLang, F.text.in_(lang_dict.LangDict["ChooseNatLangBut"]))
async def reset_natLang(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.chooseNatLangText,
        reply_markup=await Keyboards.choose_lang()
    )
    await state.set_state(BotState.Start)


@router.message(BotState.NatLang, F.text)
async def catch_text(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageDifferentTextLoc"][get_element.get_natLangID(message.from_user.id)])


@router.message(BotState.NatLang)
async def catch_obj(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageDifferentObjLoc"][get_element.get_natLangID(message.from_user.id)])