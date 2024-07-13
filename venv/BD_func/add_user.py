from aiogram.types import Message
from BD_func import connect

import lang_dict


@connect.connectAndExecute
def new_user(cur, message: Message):
    t_ID = message.from_user.id
    nickname = message.from_user.username
    f_name = message.from_user.first_name
    l_name = message.from_user.last_name
    
    for i in range(len(lang_dict.LangDict["Lang"])):
        if message.text == lang_dict.LangDict["LangBig"][i]:
            n_langID = i
            t_langID = i
            n_lang = lang_dict.LangDict["Lang"][i]
            t_lang = lang_dict.LangDict["Lang"][i]
            break
    chat_ID = str(message.from_user.id)+str(n_lang)

    sql = """INSERT INTO users (telegram_id, nick_name, first_name, last_name, native_lang, trein_lang, native_lang_id, trein_lang_id, chat_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    cur.execute(sql, (t_ID, nickname, f_name, l_name, n_lang, t_lang, n_langID, t_langID, chat_ID))
    
    return True

