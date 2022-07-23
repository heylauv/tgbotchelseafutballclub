from aiogram import Bot
from aiogram import Dispatcher
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()


bot = Bot(token="5530847718:AAHSoBqj8PosgbXaJJB--3k9ut0DgSoOlOk")
dp = Dispatcher(bot,storage=storage)
