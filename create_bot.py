from aiogram import Bot
from aiogram import Dispatcher
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()


URL_APP="https://chelseabottg.herokuapp.com/"

bot = Bot(token="5530847718:AAHSoBqj8PosgbXaJJB--3k9ut0DgSoOlOk")
dp = Dispatcher(bot,storage=storage)

async def on_startup(dp):
    await bot.set_webhook(URL_APP)

async def on_shutdown(dp):
    await bot.dekete_webhook()
