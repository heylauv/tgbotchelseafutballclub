from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


b1= KeyboardButton ('/Помощь 🆙')
b2= KeyboardButton ('/След.матч ⚔ ')
b3= KeyboardButton ('/Таблица АПЛ 📜')
b4= KeyboardButton ('/Игроки Челси 💂‍♂️')
b5= KeyboardButton ('/О боте 📌')
b6= KeyboardButton ('/Правила ❗')
b7= KeyboardButton ('/Воспоминания ✨')
b8=KeyboardButton ('/YouTube 🎬')

kb_users = ReplyKeyboardMarkup (resize_keyboard=True )

kb_users.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7).row(b8)
