from aiogram import types , Dispatcher
from create_bot import bot
from create_bot import dp
from keyboards import kb_users
from data_base import sqlite_db
from keyboards import urlkbuser1 , urlkbuser2 ,urlkbuser3


#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет,самый преданный болельщик Челси,<3\nКоманды бота /help', reply_markup=kb_users)



async def command_bot (message:types.Message) :
        await message.reply ('Хочешь узнать больше инфы обо мне и о Челси?\nТогда тебе в ЛС!\n@StamfordLionBot')


#@dp.message_handler(commands=['хелп'])
async def command_help (message: types.Message):
    await bot.send_message(message.from_user.id, '/start-Бот вкл\n/help-Команды бота\n/match-Показывает след.матч\n/table-Таблица АПЛ\n/players-Игроки фк"Челси"\n/about-Инфа о боте\n/rules-Правила чата\n/memories-Воспоминания связанные с Челси.')


#@dp.message_handler(commands=['матч'])
async def command_match (message: types.Message):
    await bot.send_message(message.from_user.id, 'Следующий матч через ...', reply_markup=urlkbuser1)


#@dp.message_handler(commands=['таблица'])
async def command_table (message: types.Message):
    await bot.send_message(message.from_user.id, 'Таблица АПЛ на текущий момент:',reply_markup=urlkbuser2)


#@dp.message_handler(commands=['игроки'])
async def command_players (message: types.Message):
    await bot.send_message(message.from_user.id, 'Текущий состав ФК "Челси":', reply_markup=urlkbuser3)


#@dp.message_handler(commands=['оботе'])
async def command_about (message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот "Стэмфорд"-талисман футбольного клуба Челси,ваш верный помошник!\nПо всем вопросам по боту сюда:\n@otherworlldly\nБолеем вместе<3\nБот умеет /help, фильтрация мата в чатах.' )


#@dp.message_handler(commands=['правила'])
async def command_rules(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПРАВИЛА ЧАТА:\nЗапрещается:\n1.Приминение открытого или заув.мата\n2.Дискриминация\n3.Пропаганда\n4.Оскорбление участников\n5.Провокация\nПРАВИЛА БУДУТ ДОПОЛНЯТЬСЯ!' )




async def command_memories(message: types.Message):
    await sqlite_db.sql_read(message)




def rg_handlers_users (dp=Dispatcher):
    dp.register_message_handler(command_start,commands=['start'])
    dp.register_message_handler(command_bot,commands=['bot'])
    dp.register_message_handler(command_help,commands=['help'])
    dp.register_message_handler(command_match,commands=['match'])
    dp.register_message_handler(command_table,commands=['table'])
    dp.register_message_handler(command_players,commands=['players'])
    dp.register_message_handler(command_about,commands=['about'])
    dp.register_message_handler(command_rules,commands=['rules'])
    dp.register_message_handler(command_memories,commands=['memories'])
