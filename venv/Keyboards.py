from aiogram import types
import lang_dict

async def choose_lang():
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["LangBig"][0])],
          [types.KeyboardButton(text=lang_dict.LangDict["LangBig"][1]), types.KeyboardButton(text=lang_dict.LangDict["LangBig"][2])]]  # список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

async def change_treinLang(langID):
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["ChooseTreinLangRusBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["ChooseTreinLangEngBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["ChooseTreinLangDeuBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["ChooseNatLangBut"][langID])]]# список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

async def go_train(langID):
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["StartDialogYesBut"][langID]), types.KeyboardButton(text=lang_dict.LangDict["StartDialogNoBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["ChooseNatLangBut"][langID]), types.KeyboardButton(text=lang_dict.LangDict["ChooseTreinLangBut"][langID])]]  # список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

async def change_natAndTreinLang(langID):
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["StartDialogYesBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["ChooseNatLangBut"][langID]), types.KeyboardButton(text=lang_dict.LangDict["ChooseTreinLangBut"][langID])]]  # список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

async def end_train(langID):
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["EndTreinBut"][langID])]]  # список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

async def get_feedback(langID):
    kb = [[types.KeyboardButton(text=lang_dict.LangDict["GetFeedbackYesBut"][langID])],
          [types.KeyboardButton(text=lang_dict.LangDict["GetFeedbackNoBut"][langID])]]  # список кнопок
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard