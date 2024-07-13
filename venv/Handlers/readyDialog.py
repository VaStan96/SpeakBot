from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, add_user, change_element, get_element
from States import BotState

import Keyboards

import lang_dict

router = Router()


@router.message(BotState.ReadyForDialog, F.text.in_(lang_dict.LangDict["StartDialogYesBut"]))
async def start_dialog(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.LangDict["AIFirstMessage"][get_element.get_treinLangID(message.from_user.id)],
        reply_markup=await Keyboards.end_train(get_element.get_treinLangID(message.from_user.id))
    )
    await state.set_state(BotState.Dialog)


@router.message(BotState.ReadyForDialog, F.text.in_(lang_dict.LangDict["StartDialogNoBut"]))
async def pause_dialog(message: Message):
    await message.answer(
        lang_dict.LangDict["StartDialogNoText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.change_natAndTreinLang(get_element.get_natLangID(message.from_user.id))
    )


@router.message(BotState.ReadyForDialog, F.text.in_(lang_dict.LangDict["ChooseNatLangBut"]))
async def reset_natLang(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.chooseNatLangText,
        reply_markup=await Keyboards.choose_lang()
    )
    await state.set_state(BotState.Start)

@router.message(BotState.ReadyForDialog, F.text.in_(lang_dict.LangDict["ChooseTreinLangBut"]))
async def reset_treinLang(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.LangDict["ChooseTreinLangText"][get_element.get_natLangID(message.from_user.id)],
        reply_markup=await Keyboards.change_treinLang(get_element.get_natLangID(message.from_user.id))
    )
    await state.set_state(BotState.NatLang)


@router.message(BotState.ReadyForDialog)
async def catch_obj(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageDifferentObjLoc"][get_element.get_natLangID(message.from_user.id)])