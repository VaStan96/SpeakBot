from aiogram.types import Message
from BD_func import connect, get_element

import lang_dict

@connect.connectAndExecute
def change_natLang(cur, message: Message):
    for i in range(len(lang_dict.LangDict["LangBig"])):
        if message.text == lang_dict.LangDict["LangBig"][i]:

            sql = """UPDATE users
                SET native_lang = %s, native_lang_id = %s
                WHERE telegram_id = %s"""

            cur.execute(sql, (lang_dict.LangDict["Lang"][i], i, str(message.from_user.id)))

            break

@connect.connectAndExecute
def change_treinLang(cur, message: Message):
    lang_id = get_element.get_natLangID(message.from_user.id)
    text = message.text

    if text == (lang_dict.LangDict["ChooseTreinLangRusBut"][lang_id]):
        trein_id = 0
    elif text == lang_dict.LangDict["ChooseTreinLangEngBut"][lang_id]:
        trein_id = 1
    elif text == lang_dict.LangDict["ChooseTreinLangDeuBut"][lang_id]:
        trein_id = 2

    sql = """UPDATE users
        SET trein_lang = %s, trein_lang_id = %s
        WHERE telegram_id = %s"""

    cur.execute(sql, (lang_dict.LangDict["Lang"][trein_id], trein_id, str(message.from_user.id)))
