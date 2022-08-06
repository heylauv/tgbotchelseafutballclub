from aiogram.types import KeyboardButton , ReplyKeyboardMarkup


button_load = KeyboardButton ('Добавить воспоминания 📺')
button_delete= KeyboardButton ('Удалить воспоминания ⚙')
button_otmena= KeyboardButton ('Отмена ❌')
button_return_user= KeyboardButton ('Главное меню ✅')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).add(button_load)
button_case_delete= ReplyKeyboardMarkup (resize_keyboard=True).add(button_delete)
button_case_otmena= ReplyKeyboardMarkup (resize_keyboard=True).add(button_otmena)
button_r_user= ReplyKeyboardMarkup (resize_keyboard=True).add(button_return_user)
