import aiohttp.web


from quotes.db import get_random_element
from quotes.serializer import json_dump


async def author_handler(request):
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = await get_random_element(db.quotes, pipeline)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')


async def random_handler(request):
    db = request.app['db']
    quote_json = await get_random_element(db.quotes)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')
