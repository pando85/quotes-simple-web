import aiohttp
from aiohttp.web import Request
import motor.motor_asyncio
import pymongo
from typing import Dict, List, Optional

from quotes.config import MONGO_URI, QUOTES_PATH
from quotes.utils import dict_from_transcript, quote_from_dict, list_files_in_directory, read_file
from quotes import logger
from quotes.quote import Quote

MongoQuery = List[Dict]


async def mongo_connection(app: aiohttp.web.Application) -> None:
    mongo = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

    async def _cleanup(app: aiohttp.web.Application) -> None:
        logger.debug('Close database connection')
        mongo.close()
    app.on_cleanup.append(_cleanup)
    app['db'] = mongo['test']


async def load_db(app: aiohttp.web.Application, path: str) -> None:
    logger.debug('Remove database collection')
    await app['db'].quotes.drop()

    logger.debug(f'Insert quotes from path `{path}`')
    data = [dict_from_transcript(read_file(file)) for file in list_files_in_directory(path)]
    await app['db'].quotes.insert_many(data)
    logger.debug('Create index by author')
    await app['db'].quotes.create_index([('author', pymongo.TEXT)])


async def setup_db(app: aiohttp.web.Application) -> None:
    await mongo_connection(app)
    await load_db(app, QUOTES_PATH)


async def get_random_quote(request: Request) -> Optional[Quote]:
    query = get_query_random()
    return await query_db(request.app['db'], query)


def get_query_filter_author(author: str) -> MongoQuery:
    filter_author = {'$match': {'$text': {'$search': author}}}
    return [filter_author]


def get_query_random() -> MongoQuery:
    random_element = {'$sample': {'size': 1}}
    return [random_element]


async def query_db(
        db: motor.motor_asyncio.AsyncIOMotorDatabase,
        pipeline: MongoQuery) -> Optional[Quote]:
    cursor = db.quotes.aggregate(pipeline)
    while (await cursor.fetch_next):
        return quote_from_dict(cursor.next_object())
    return None
