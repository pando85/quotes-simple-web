import aiohttp
import json
import motor.motor_asyncio
import pymongo

from quotes.config import AUDIO_DIR_PATH, MONGO_URI, QUOTES_FILE_PATH
from quotes.utils import add_audio_to_json
from quotes.logger import logger


async def mongo_connection(app):
    mongo = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

    async def _cleanup(app):
        logger.debug('Close database connection')
        mongo.close()
    app.on_cleanup.append(_cleanup)
    app['db'] = mongo['test']


async def load_db(app, path: str):
    logger.debug('Remove database collection')
    await app['db'].quotes.drop()
    with open(path) as f:
        data = json.load(f)
    logger.debug(f'Insert quotes from file `{path}`')
    await app['db'].quotes.insert_many(data)
    logger.debug('Create index by author')
    await app['db'].quotes.create_index([('author', pymongo.TEXT)])


async def setup_db(app):
    await mongo_connection(app)
    await load_db(app, QUOTES_FILE_PATH)
    await add_audio_to_json(app['db'], AUDIO_DIR_PATH)


async def get_random_element(collection, pipeline=[]):
    random_element = {'$sample': {'size': 1}}
    pipeline.append(random_element)
    cursor = collection.aggregate(pipeline)
    while (await cursor.fetch_next):
        return cursor.next_object()
    return None
