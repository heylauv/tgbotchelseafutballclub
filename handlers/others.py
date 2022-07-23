from aiogram import types , Dispatcher
import json , string
from create_bot import dp


#@dp.message_handler()
async def filter_mates(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenzura.json')))) != set():
        await message.reply('Не матерись!\nДо добра не доведет<3')
        await message.delete()

def rg_handlers_others (dp=Dispatcher):
    dp.register_message_handler(filter_mates)
