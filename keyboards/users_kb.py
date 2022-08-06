from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


b1= KeyboardButton ('/Помощь🆙')
b2= KeyboardButton ('/Матч⚔ ')
b3= KeyboardButton ('/Таблица_АПЛ📜')
b4= KeyboardButton ('/Игроки_Челси💂‍♂️')
b5= KeyboardButton ('/Бот📌')
b6= KeyboardButton ('/Правила❗')
b7= KeyboardButton ('/Воспоминания✨')
b8=KeyboardButton ('/YouTube🎬')

kb_users = ReplyKeyboardMarkup (resize_keyboard=True )

kb_users.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).row(b7).row(b8)
