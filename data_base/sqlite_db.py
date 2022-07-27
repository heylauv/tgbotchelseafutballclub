
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
    cur.execute (
    """CREATE TABLE IF NOT EXISTS memories(
        img varchar (50) NOT NULL,
        name varchar (100) PRIMARY KEY,
        discruption varchar (200) NOT NULL);"""
        )
    base.cursor()
    base.commit()

async def add_sql_command(state):
    global base , cur
    async with state.proxy() as data:
        cur.execute (
            """INSERT INTO memories (img , name , discruption) VALUES
            (' ? ',' ? ',' ? ' ); """ , tuple(data.values()))
        base.commit()

async def sql_read(message):
    global base , cur
    for ret in cur.execute('SELECT * FROM memories').fetchone():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    global base , cur
    return cur.execute ('SELECT * FROM memories').fetchone()

async def sql_delete_command(data):
    global base , cur
    cur.execute ('DELETE FROM memories WHEN name == ?', (data,))
    base.commit()
