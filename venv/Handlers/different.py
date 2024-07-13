from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove

from BD_func import check_user, add_user, change_element, get_element
import lang_dict

router = Router()

@router.message(F.text)
async def set_fehler(message: Message):
    await message.answer(lang_dict.LangDict["FehlerMessageMenu"][get_element.get_natLangID(message.from_user.id)])