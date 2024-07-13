from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from BD_func import check_user, get_element
from States import BotState
import Keyboards

import lang_dict

router = Router()

@router.message(Command("start"))
@router.message(F.text =="start")
async def cmd_start(message: Message, state: FSMContext):
    if not check_user.check_user(message.from_user.id):
        await message.answer(
            lang_dict.startHelloText
        )
    await cmd_change_natLang(message, state)

@router.message(Command("help"))
@router.message(F.text =="help")
async def cmd_help(message: Message, state: FSMContext):
    if check_user.check_user(message.from_user.id):
        await message.answer(
            lang_dict.LangDict["HelpText"][get_element.get_natLangID(message.from_user.id)]
        )
    else:
        await message.answer(
            lang_dict.HelpSmallText
        )


@router.message(Command("change"))
@router.message(F.text =="change")
async def cmd_change_treinLang(message: Message, state: FSMContext):
    if check_user.check_user(message.from_user.id):
        await message.answer(
            lang_dict.LangDict["ChooseTreinLangText"][get_element.get_natLangID(message.from_user.id)],
            reply_markup= await Keyboards.change_treinLang(get_element.get_natLangID(message.from_user.id))
        )
        await state.set_state(BotState.NatLang)
    else:
        await cmd_change_natLang(message)


@router.message(Command("changeLang"))
@router.message(F.text =="changeLang")
async def cmd_change_natLang(message: Message, state: FSMContext):
    await message.answer(
        lang_dict.chooseNatLangText,
        reply_markup= await Keyboards.choose_lang()
    )
    await state.set_state(BotState.Start)
