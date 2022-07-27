
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from create_bot import bot , dp
from create_bot import URL_APP

import os

async def on_startup(dp):
    await bot.set_webhook(URL_APP)
    print ('Бот вкл,успешной работы!')
    await sqlite_db.sql_start()


async def on_shutdown(dp):
    await bot.delete_webhook()


from handlers import users , admins , others
import inline

users.rg_handlers_users(dp)
admins.register_handler_admins (dp)
others.rg_handlers_others(dp)
inline.rg_inline_handler(dp)



executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)))
