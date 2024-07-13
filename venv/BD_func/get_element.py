from BD_func import connect
from aiogram.types import Message

@connect.connectAndExecute
def get_natLang(cur, TelegrammID) -> str:

    sql = """SELECT native_lang
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return str(result[0])

@connect.connectAndExecute
def get_treinLang(cur, TelegrammID) -> str:
    sql = """SELECT trein_lang
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return str(result[0])

@connect.connectAndExecute
def get_chatID(cur, TelegrammID) -> str:
    sql = """SELECT chat_id
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return str(result[0])

@connect.connectAndExecute
def get_name(cur, TelegrammID) -> str:
    sql = """SELECT first_name, last_name
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    l_name = str(cur.fetchone()[0])
    f_name = str(cur.fetchone()[0])
    result = ' '.join(f_name, l_name)
    return result

@connect.connectAndExecute
def get_nickname(cur, TelegrammID) -> str:
    sql = """SELECT nick_name
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return str(result[0])

@connect.connectAndExecute
def get_telegrammID(cur, Nickname = None, fName = None, lName = None) -> str:
    if Nickname != None:
        sql = """SELECT native_lang_id
            FROM users
            WHERE nick_name = %s"""
        cur.execute(sql, (Nickname,))
        result = cur.fetchone()
    elif fName != None and lName != None:
        sql = """SELECT native_lang_id
            FROM users
            WHERE first_name = %s, last_name = %s"""
        cur.execute(sql, (fName, lName))
        result = cur.fetchone()
    else:
        result = None

    return str(result[0])

@connect.connectAndExecute
def get_natLangID(cur, TelegrammID) -> int:
    sql = """SELECT native_lang_id
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return int(result[0])

@connect.connectAndExecute
def get_treinLangID(cur, TelegrammID) -> int:
    sql = """SELECT trein_lang_id
        FROM users
        WHERE telegram_id = %s"""

    cur.execute(sql, (str(TelegrammID),))
    result = cur.fetchone()
    return int(result[0])