from optparse import Values
from os import curdir
import sqlite3 as sq
from unicodedata import name
from weakref import proxy
from create_bot import bot

def sql_start():
    global base , cur
    base= sq.connect('event_cfc.db')
    cur=base.cursor()
    if base:
        print ('Подключились к базе данных!')
    base.execute ('CREATE TABLE IF NOT EXISTS events(img TEXT, name TEXT PRIMARY KEY, discruption TEXT)' )
    base.cursor()

async def add_sql_command(state):
    async with state.proxy() as data:
        cur.execute ('INSERT OR REPLACE INTO events VALUES ( ?, ?, ? )', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM events').fetchall():
        await bot.send_photo(message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret[2]}\nНадеюсь вам понравилось воспоминание!')

async def sql_read2():
    return cur.execute ('SELECT * FROM events').fetchall()

async def sql_delete_command(data):
    cur.execute ('DELETE FROM events WHEN neame == ?', (data,))
    base.commit()
