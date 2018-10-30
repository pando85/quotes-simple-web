import aiohttp.web


from quotes.db import get_random_element
from quotes.serializer import json_dump
from quotes.logger import logger


async def author_handler(request):
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = await get_random_element(db.quotes, pipeline)
    return response(quote_json)


async def random_handler(request):
    db = request.app['db']
    quote_json = await get_random_element(db.quotes)
    return response(quote_json)


def response(quote_json):
    logger.debug(quote_json)
    if not quote_json:
        raise aiohttp.web.HTTPNotFound()
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')
