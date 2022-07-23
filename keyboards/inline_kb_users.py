
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

urlkbuser1 = InlineKeyboardMarkup (row_width=1)

urlbutton1 = InlineKeyboardButton (text='Матч', url='https://inlnk.ru/4yD778')
urlkbuser1.add(urlbutton1)

urlkbuser2 = InlineKeyboardMarkup (row_width=1)

urlbutton2 = InlineKeyboardButton (text= 'Таблица', url='https://inlnk.ru/4yD7X8')
urlkbuser2.add(urlbutton2)

urlkbuser3 = InlineKeyboardMarkup (row_width=1)

urlbutton3 = InlineKeyboardButton (text='Состав', url='https://inlnk.ru/za74VV')
urlkbuser3.add(urlbutton3)
