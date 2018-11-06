import aiohttp
import json
import motor.motor_asyncio
import pymongo
from typing import Optional

from quotes.config import MONGO_URI, QUOTES_FILE_PATH
from quotes.utils import dict_to_quote
from quotes.logger import logger
from quotes.quote import Quote


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
    with open(path) as f:
        data = json.load(f)
    logger.debug(f'Insert quotes from file `{path}`')
    await app['db'].quotes.insert_many(data)
    logger.debug('Create index by author')
    await app['db'].quotes.create_index([('author', pymongo.TEXT)])


async def setup_db(app: aiohttp.web.Application) -> None:
    await mongo_connection(app)
    await load_db(app, QUOTES_FILE_PATH)


async def get_random_element(
        collection: motor.motor_asyncio.AsyncIOMotorCollection,
        pipeline: list = []) -> Optional[Quote]:
    random_element = {'$sample': {'size': 1}}
    pipeline.append(random_element)
    cursor = collection.aggregate(pipeline)
    while (await cursor.fetch_next):
        return dict_to_quote(cursor.next_object())
    return None
