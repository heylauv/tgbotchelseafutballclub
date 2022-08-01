
from create_bot import bot
import psycopg2
from data_base.config import host , user , password , database
#from psycopg2.errorcodes import UNIQUE_VIOLATION
#from psycopg2 import errors

base= psycopg2.connect (
        host=host ,
        user=user ,
        password=password ,
        database=database
        )
base.autocommit=True
cur = base.cursor()

async def sql_start():
    if base:
         print ('Я подключился!')
    cur.execute (
     """CREATE TABLE IF NOT EXISTS memorycfcb(
        photo TEXT  NOT NULL,
        name TEXT NOT NULL,
        description TEXT  NOT NULL);"""
     )
    base.cursor()

async def add_sql_command(state):
    #try:
        async with state.proxy() as data:
            cur.execute(
        """INSERT INTO memorycfcb (photo , name , description) VALUES
        (%s, %s, %s); """ , tuple(data.values()))
    #except errors.lookup(UNIQUE_VIOLATION) as e:
        #print (e)


async def sql_read(message):
    cur.execute('SELECT * FROM memorycfcb')
    for ret in cur.fetchall():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    cur.execute('SELECT * FROM memorycfcb')
    return cur.fetchall()


async def sql_delete_command(data):
    cur.execute ('DELETE FROM memorycfcb WHERE name == %s', (data,))
