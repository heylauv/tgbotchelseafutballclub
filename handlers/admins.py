
from asyncore import read
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram import types , Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp , bot
from data_base import sqlite_db
from data_base.sqlite_db import add_sql_command
from keyboards import admins_kb
from aiogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
from data_base.sqlite_db import sql_delete_command

ID=None

async def make_changes_command(message:types.Message):
    global ID
    ID=message.from_user.id
    await bot.send_message(message.from_user.id , 'Приветствую начальство.\nЧто делаем?' , reply_markup=admins_kb.button_case_admin )
    await message.delete()

class FSMAdmin(StatesGroup):
    photo=State()
    name= State()
    discription=State()

#@dp.message_handler(commands="Events", state=None)
async def cm_memories_show(message:types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply ('Загрузи фото')

async def otmena_command(message:types.Message , state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply ('Окей')


#@dp.message_handler (content_types=['photo'],State=FSMAdmin.photo)
async def up_photo(message:types.Message , state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data ['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply ('Название фото:')

#@dp.message_handler(state=FSMAdmin.name)
async def cm_name(message:types.Message , state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['names']=message.text
        await FSMAdmin.next()
        await message.reply ('Описание:')


#@dp.message_hendler ( state=FSMAdmin.discruption)
async def cm_discription (message:types.Message , state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data ['discription']=message.text
        await bot.send_message(message.from_user.id , 'Событие указано!')

        await add_sql_command(state)
        await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callbeck_run(callbeck_query: types.CallbackQuery):
    await sql_delete_command (callbeck_query.data.replace('del ', ''))
    await callbeck_query.answer (text=f' {callbeck_query.data.replace ("del ", "")} удалена. ' , show_alert=True )


@dp.message_handler (commands='memoriesdell')
async def memories_dell (message:types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo (message.from_user.id , ret[0], f'{ret[1]}\nОписание:\n{ret [2]}\nНадеюсь вам понравилось воспоминание! ', reply_markup=admins_kb.button_case_delete )
            await bot.send_message (message.from_user.id , text='Удалить это?', reply_markup=InlineKeyboardMarkup().\
                    add(InlineKeyboardButton(f' Удалить {ret[1]}', callback_data= f'del {ret[1]}')))





def register_handler_admins (dp : Dispatcher):
    dp.register_message_handler(make_changes_command,commands=['adm'], is_chat_admin=True)
    dp.register_message_handler(cm_memories_show, commands=['Добавить воспоминания 📺'],state=None)
    dp.register_message_handler (otmena_command , state="*", commands= ['Отмена'] , reply_markup=admins_kb.button_case_otmena)
    dp.register_message_handler (otmena_command , Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(up_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(cm_name,state=FSMAdmin.name)
    dp.register_message_handler(cm_discription,state=FSMAdmin.discription)
