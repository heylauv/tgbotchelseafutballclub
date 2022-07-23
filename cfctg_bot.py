
from aiogram.utils import executor
from create_bot import dp, on_shutdown
from data_base import sqlite_db
import os


async def on_startup(_):
    print('Бот запущен,успешной работы.')
    sqlite_db.sql_start()



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
