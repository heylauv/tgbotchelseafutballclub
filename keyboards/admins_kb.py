from aiogram.types import KeyboardButton , ReplyKeyboardMarkup


button_load = KeyboardButton ('Добавить воспоминания 📺')
button_delete= KeyboardButton ('Удалить воспоминания ⚙')
button_otmena= KeyboardButton ('Отмена ❌')
button_return_user= KeyboardButton ('Меню пользователя ✅')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).add(button_load).row(button_delete).add(button_otmena).row(button_return_user)
