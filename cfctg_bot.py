
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот запущен,успешной работы.')
    sqlite_db.sql_start()



from handlers import users , admins , others
import inline

users.rg_handlers_users(dp)
admins.register_handler_admins (dp)
others.rg_handlers_others(dp)
inline.rg_inline_handler(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
