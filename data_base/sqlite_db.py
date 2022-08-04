
from create_bot import bot
import psycopg2
from data_base.config import host , user , password , database

base= psycopg2.connect (
        host=host ,
        user=user ,
        password=password ,
        database=database
        )
cur = base.cursor()
try:
    async def sql_start():
        if base:
             print ('Я подключился!')
        cur.execute (
        """CREATE TABLE IF NOT EXISTS cfc(
        photo TEXT  NOT NULL,
        name TEXT primary key NOT NULL,
        description TEXT  NOT NULL);"""
        )
        #base.cursor()
        base.commit()

    async def add_sql_command(state):
        async with state.proxy() as data:
            cur.execute(
                """INSERT INTO cfc (photo , name , description) VALUES
                (%s, %s, %s); """ , tuple(data.values()))
            base.commit()

    async def sql_read(message):
        cur.execute('SELECT * FROM cfc')
        for ret in cur.fetchall():
            await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')


    async def sql_read2():
        cur.execute('SELECT * FROM cfc')
        return cur.fetchall()


    async def sql_delete_command(data):
        cur.execute('DELETE FROM cfc WHERE name= %s', (data, ))
        base.commit()

except Exception as er:
    print (er)
finally:
    print ('DB closed.')
