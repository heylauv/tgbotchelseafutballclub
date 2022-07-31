
from create_bot import bot
import psycopg2
from data_base.config import host , user , password , database
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors

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
     """CREATE TABLE IF NOT EXISTS memcfc(
        photo TEXT  NOT NULL,
        name varchar (100) PRIMARY KEY,
        discription TEXT  NOT NULL);"""
     )
    base.cursor()

async def add_sql_command(state):
    #try:
        async with state.proxy() as data:
            cur.execute(
        """INSERT INTO memcfc (photo , name , discription) VALUES
        ( ? , ? , ? ); """ , tuple(data.values()))
    #except errors.lookup(UNIQUE_VIOLATION) as e:
        #print (e)


async def sql_read(message):
    cur.execute('SELECT * FROM memcfc')
    for ret in cur.fetchall():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    return cur.execute ('SELECT * FROM memcfc') , cur.fetchall()


async def sql_delete_command(data):
    cur.execute ('DELETE FROM memcfc WHEN name == ?', (data,))
