from aiogram import types , Dispatcher
from create_bot import bot
from create_bot import dp
from keyboards import kb_users
from data_base import sqlite_db
from keyboards import urlkbuser1 , urlkbuser2 ,urlkbuser3 ,urlstream4


#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет,самый преданный болельщик Челси<3\nКоманды бота /help', reply_markup=kb_users)


async def command_bot (message:types.Message) :
        await message.reply ('Хочешь узнать больше инфы обо мне и о Челси?\nТогда тебе в ЛС<3\n@StamfordLionBot')

async def command_help (message: types.Message):
    await bot.send_message(message.from_user.id, 'КОМАНДЫ:\n/help-Что бот умеет.\n/adm-Для админов(в чате).\n/bot-Инфо в ЛС(в чатах)\nКНОПКИ:\nМатч⚔- Показывает след.матч.\nТаблица📜- Таблица АПЛ на текущий момент.\nСостав💂‍♂️- Игроки фк"Челси".\nБот📌- Инфа о боте.\nПравила❗- Правила чата.\nВоспоминания✨- Воспоминания связанные с Челси.\nYouTube🎬- Поиск видео в Ютубе.\nТрансляция⚽- Ссылка на матч(Не ручаюсь за валидность.)')

#@dp.message_handler(commands=['хелп'])
#async def command_ (message: types.Message):
 #   await bot.send_message(message.from_user.id, 'Матч⚔- Показывает след.матч.\nТаблица📜- Таблица АПЛ на текущий момент.\nСостав💂‍♂️- Игроки фк"Челси".\nБот📌- Инфа о боте.\nПравила❗- Правила чата.\nВоспоминания✨- Воспоминания связанные с Челси.\nYouTube🎬- Поиск видео в Ютубе.')


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
    await bot.send_message(message.from_user.id, 'Стэмфорд-талисман футбольного клуба Челси и ваш верный помошник!\nБот так же умеет фильтровать мат в чатах.' )


#@dp.message_handler(commands=['правила'])
async def command_rules(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПРАВИЛА ЧАТА:\nЗапрещается:\n1.Приминение открытого или заув.мата\n2.Дискриминация\n3.Пропаганда\n4.Оскорбление участников\n5.Провокация\nПРАВИЛА БУДУТ ДОПОЛНЯТЬСЯ!' )


async def command_youtube(message:types.Message):
    await bot.send_message(message.from_user.id,'Бот умеет искать видео в YouTube!\nПропишите @StamfordLionBot и название видео.\nРаботает как в лс так и чатах!')

async def command_stream (message: types.Message):
    await bot.send_message(message.from_user.id, 'Трансляция:', reply_markup=urlstream4)

async def command_memories(message: types.Message):
    await sqlite_db.sql_read(message)




def rg_handlers_users (dp=Dispatcher):
    dp.register_message_handler(command_start,commands=['start'])
    dp.register_message_handler(command_bot,commands=['bot'])
    dp.register_message_handler(command_help,commands=['help'])
    #dp.register_message_handler(command_helps,commands=['Помощь🆙'])
    dp.register_message_handler(command_match,commands=['Матч⚔'])
    dp.register_message_handler(command_table,commands=['Таблица📜'])
    dp.register_message_handler(command_players,commands=['Состав💂‍♂️'])
    dp.register_message_handler(command_about,commands=['Бот📌'])
    dp.register_message_handler(command_rules,commands=['Правила❗'])
    dp.register_message_handler(command_youtube,commands=['YouTube🎬'])
    dp.register_message_handler(command_stream,commands=['Трансляция⚽'])
    dp.register_message_handler(command_memories,commands=['Воспоминания✨'])
