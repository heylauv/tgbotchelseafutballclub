
from create_bot import bot
import psycopg2
from data_base.config import host , user , password , database

try:
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
        """CREATE TABLE IF NOT EXISTS memorydates(
        photos TEXT  NOT NULL,
        namess varchar (100) PRIMARY KEY,
        discriptions TEXT  NOT NULL);"""
        )
        base.cursor()

    async def add_sql_command(state):
        async with state.proxy() as data:
                cur.execute(
            """INSERT INTO memorydates (photos , namess , discriptions) VALUES
            ( ? , ? , ? ); """ , tuple(data.values()))

    async def sql_read(message):
        cur.execute('SELECT * FROM memorydates')
        for ret in cur.fetchall():
            await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

    async def sql_read2():
        return cur.execute ('SELECT * FROM memorydates') , cur.fetchall()


    async def sql_delete_command(data):
        cur.execute ('DELETE FROM memorydates WHEN name == ?', (data,))

except Exception as _ex:
    print ('INFO', _ex)
finally:
    if base:
        print('Включаюсь!')
