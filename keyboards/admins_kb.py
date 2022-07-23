from aiogram.types import KeyboardButton , ReplyKeyboardMarkup


button_load = KeyboardButton ('/memoriesupdate')
button_delete= KeyboardButton ('/memoriesdell')
button_otmena= KeyboardButton ('/отмена')
button_return_user= KeyboardButton ('/start')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).add(button_load)\
            .add(button_delete).add(button_otmena).add(button_return_user)
