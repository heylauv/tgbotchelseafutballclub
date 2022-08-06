from aiogram.types import KeyboardButton , ReplyKeyboardMarkup


button_load = KeyboardButton ('/Воспоминание➕')
button_delete= KeyboardButton ('/Воспоминание➖')
#button_otmena= KeyboardButton ('/Отмена❌')
button_return_user= KeyboardButton ('/Меню✅')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).row(button_load).row(button_delete).row(button_return_user)
