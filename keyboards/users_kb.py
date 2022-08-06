from termios import B50
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


b6= KeyboardButton ('/Трансляция⚽')
b3= KeyboardButton ('/Матч⚔')
b4= KeyboardButton ('/Таблица📜')
b5= KeyboardButton ('/Состав💂‍♂️')
b1= KeyboardButton ('/Бот📌')
b2= KeyboardButton ('/Правила❗')
b7= KeyboardButton ('/Воспоминания✨')
b8=KeyboardButton ('/YouTube🎬')

kb_users = ReplyKeyboardMarkup (resize_keyboard=True )

kb_users.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7).insert(b8)
