from os import link
from aiogram import  types , Dispatcher
import hashlib
from create_bot import dp
from aiogram.types import InputTextMessageContent , InlineQueryResultArticle
from youtube_search import YoutubeSearch



def searcher (text):
    res=YoutubeSearch (text , max_results=10).to_dict()
    return res

#@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id = hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title = f'{link["title"]}',
        url = f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content = types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}' )
        )    for link in links]

    await query.answer(articles, cache_time=33, is_personal=True)

def rg_inline_handler (dp=Dispatcher):
    dp.register_inline_handler(inline_handler)
