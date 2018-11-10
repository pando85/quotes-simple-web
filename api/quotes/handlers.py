from aiohttp.web import Request, Response
from typing import Optional

from quotes.db import get_author_random_quote, get_random_quote
from quotes.logger import logger
from quotes.serializer import quote_to_json


async def author_handler(request: Request) -> Response:
    quote = await get_author_random_quote(request)
    _json = quote_to_json(quote)
    logger.debug(_json)
    return return_response(_json)
#    return await compose(
#        get_author_random_quote,
#        quote_to_json,
#        logger.debug,
#        return_response)(request)


async def ping_handler(request: Request) -> Response:
    return Response(body='"pong"', content_type='application/json')


async def random_handler(request: Request) -> Response:
    quote = await get_random_quote(request)
    _json = quote_to_json(quote)
    logger.debug(_json)
    return return_response(_json)
#    return await compose(
#        get_random_quote,
#        quote_to_json,
#        logger.debug,
#        return_response)(request)


def return_response(_json: Optional[str]) -> Response:
    msg = _json
    status_code = 200
    if not _json:
        msg = '{"error": "Not quote found"}'
        status_code = 500
    return Response(body=msg, content_type='application/json', status=status_code)
