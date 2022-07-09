
from email import message
from email.message import Message
from posixpath import split
import string
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import json

bot = Bot(token="5530847718:AAHSoBqj8PosgbXaJJB--3k9ut0DgSoOlOk")
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен,успешной работы.')


@dp.message_handler(commands=['start']) # Человек прописал старт в общем чате ему бот по идее написать в ЛС , а если закрыто то ответить в reply,но почему то от всегда делает через reply
async def command_start(message: types.Message):
    try:
        await bot.send.message(message.from_user.id, 'Привет,самый преданный болельщик Челси,<3\nКоманды бота /help')
        await message.delete()
    except:
        await message.reply('Привет,дополонительная информация по боту в ЛС /хелп ,напишите ему:@StamfordLionBot ')

# Вот эти все команды человек уже пишет в лс боту , но они работают как то через раз,то нормально ответит то через первый хендлер в reply
@dp.message_handler(commands=['хелп'])
async def command_help (message: types.Message):
    await bot.send_message(message.from_user.id, '/start-Бот вкл\n/хелп-Команды бота,\n/матч-Показывает след.матч,\n/таблица-Таблица АПЛ,\n/игроки-Игроки фк"Челси"\n/бот-Инфа о боте\n/правила-Правила...')


@dp.message_handler(commands=['матч'])
async def command_natch (message: types.Message):
    await bot.send_message(message.from_user.id, 'Следующий матч через ...')


@dp.message_handler(commands=['таблица'])
async def command_table (message: types.Message):
    await bot.send_message(message.from_user.id, 'Таблица АПЛ на текущий момент:')


@dp.message_handler(commands=['игроки'])
async def command_players (message: types.Message):
    await bot.send_message(message.from_user.id, 'Текущий состав ФК "Челси":')


@dp.message_handler(commands=['бот'])
async def command_about (message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот "Стэмфорд"-талисман футбольного клуба Челси,\nПо всем вопросам по боту сюда:\n@otherworlldly\nБолеем вместе<3\nБот умеет /хелп, фильтрация мата.')


@dp.message_handler(commands=['правила'])
async def command_rules(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПРАВИЛА ЧАТА:\nЗапрещается:\n1.Приминение открытого или заув.мата\n2.Дискриминация\n3.Пропаганда\n4.Оскорбление участников\n5.Провокация\nПРАВИЛА БУДУТ ДОПОЛНЯТЬСЯ!')


@dp.message_handler()
async def echobot_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Не матерись!\nДо добра не доведет<3')
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
