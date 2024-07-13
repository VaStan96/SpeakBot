from BD_func import connect

@connect.connectAndExecute
def check_user(cur, TelegrammID) -> bool:

    sql = """SELECT telegram_id
        FROM users"""

    cur.execute(sql)

    users = []
    row = cur.fetchone()
    while row is not None:
        users.append(row[0])
        row = cur.fetchone()

    if str(TelegrammID) in users:
        return True
    else:
        return False