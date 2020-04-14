from aiohttp.web import Request, Response
from typing import Optional

from quotes.db import get_random_quote
from quotes.functools import compose
from quotes import logger
from quotes.serializer import quote_to_json


async def ping_handler(request: Request) -> Response:
    return compose(
        logger.debug,
        return_response)('"pong"')


async def random_handler(request: Request) -> Response:
    return await compose(
        get_random_quote,
        quote_to_json,
        logger.debug,
        return_response
    )(request)


def return_response(_json: Optional[str]) -> Response:
    msg = _json
    status_code = 200
    if not _json:
        msg = '{"error": "Not quote found"}'
        status_code = 500
    return Response(
        body=msg,
        content_type='application/json',
        headers={'Cache-Control': 'no-cache'},
        status=status_code,
    )
