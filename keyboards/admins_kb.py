from aiogram.types import KeyboardButton , ReplyKeyboardMarkup


button_load = KeyboardButton ('/Добавить_воспоминание📺')
button_delete= KeyboardButton ('/Удалить_воспоминание⚙')
button_otmena= KeyboardButton ('/Отмена❌')
button_return_user= KeyboardButton ('/Меню_пользователя✅')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).row(button_load).row(button_delete).add(button_otmena).row(button_return_user)
