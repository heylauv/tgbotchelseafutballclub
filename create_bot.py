from os import environ
from sqlite3 import connect
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()


URL_APP="https://chelseabottg.herokuapp.com/"

bot = Bot(token="5530847718:AAHSoBqj8PosgbXaJJB--3k9ut0DgSoOlOk")
dp = Dispatcher(bot,storage=storage)
