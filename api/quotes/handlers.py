from aiohttp.web import Request, Response
from typing import Optional

from quotes.db import get_random_element
from quotes.logger import logger
from quotes.quote import Quote
from quotes.serializer import quote_to_json


async def author_handler(request: Request) -> Response:
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = await get_random_element(db.quotes, pipeline)
    return response(quote_json)


async def random_handler(request: Request) -> Response:
    db = request.app['db']
    quote_json = await get_random_element(db.quotes)
    return response(quote_json)


def response(quote: Optional[Quote])-> Response:
    logger.debug(quote)
    status = 200
    if not quote:
        status = 500
    return Response(body=quote_to_json(quote), content_type='application/json', status=status)
