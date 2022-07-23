from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


b1= KeyboardButton ('/help')
b2= KeyboardButton ('/match')
b3= KeyboardButton ('/table')
b4= KeyboardButton ('/players')
b5= KeyboardButton ('/about')
b6= KeyboardButton ('/rules')
b7= KeyboardButton ('/memories')

kb_users = ReplyKeyboardMarkup (resize_keyboard=True )

kb_users.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7)
