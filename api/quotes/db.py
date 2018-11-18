import aiohttp
from aiohttp.web import Request
from random import randint
from typing import List, Optional, TypeVar

from quotes.config import QUOTES_PATH
from quotes.utils import dict_from_transcript, quote_from_dict, list_files_in_directory, read_file
from quotes import logger
from quotes.quote import Quote

T = TypeVar('T')


async def setup_db(app: aiohttp.web.Application) -> None:
    path = QUOTES_PATH
    logger.debug(f'Insert quotes from path `{path}`')
    app['db'] = [quote_from_dict(dict_from_transcript(read_file(file)))
                 for file in list_files_in_directory(path)]


async def get_random_quote(request: Request) -> Optional[Quote]:
    quotes = request.app['db']
    quote = get_random_value(quotes)
    return quote


def get_random_value(_list: List[T]) -> T:
    return _list[randint(0, len(_list) - 1)]
