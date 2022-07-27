
from create_bot import bot
import psycopg2
from data_base.config import host , user , password , database



async def sql_start():
    global base , cur
base= psycopg2.connect (
    host=host ,
    user=user ,
    password=password ,
    database=database
)
cur = base.cursor()
if base:
    print ('Я подключился!')
    cur.execute ('CREATE TABLE IF NOT EXISTS memories(img TEXT, name TEXT PRIMARY KEY, discruption TEXT)' )
    base.cursor()

async def add_sql_command(state):
    global base , cur
    async with state.proxy() as data:
        cur.execute ('INSERT INTO memories VALUES ( ?, ?, ? )', tuple(data.values()))
        base.commit()

async def sql_read(message):
    global base , cur
    for ret in cur.execute('SELECT * FROM memories').fetchall():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    global base , cur
    return cur.execute ('SELECT * FROM memories').fetchall()

async def sql_delete_command(data):
    global base , cur
    cur.execute ('DELETE FROM memories WHEN name == ?', (data,))
    base.commit()
