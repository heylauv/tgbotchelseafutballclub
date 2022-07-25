
from weakref import proxy
from create_bot import bot
import psycopg2 as ps
import os

async def sql_start():
    global cur , base
    base= ps.connect (os.environ.get('DATABASE_URL') , sslmode='require')
    cur=base.cursor()
    if base:
        print ('Подключились к базе данных!')
    #base.execute ('CREATE TABLE IF NOT EXISTS eventts(img TEXT, name TEXT PRIMARY KEY, discruption TEXT)' )
    #base.cursor()

async def add_sql_command(state):
    async with state.proxy() as data:
        cur.execute ('INSERT OR REPLACE INTO eventt VALUES ( ?, ?, ? )', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM eventt').fetchall():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    return cur.execute ('SELECT * FROM eventt').fetchall()

async def sql_delete_command(data):
    cur.execute ('DELETE FROM eventt WHEN name == ?', (data,))
    base.commit()
