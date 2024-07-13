import functools
import psycopg
from settings import Secret

def connectAndExecute(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            #connecting to the PostgreSQL server
            with psycopg.connect(
                    host = Secret.DBhost,
                    dbname = Secret.DBdatabase,
                    user = Secret.DBuser,
                    password = Secret.DBpassword
            ) as conn:
                #log
                print ('Connected to the PostgreSQL server.')
                #создаем курсор
                with conn.cursor() as cur:
                    result = func(cur, *args, **kwargs)
                    conn.commit()
                    return result
        except (psycopg.DatabaseError, Exception) as error:
            print(error)
    return wrapper