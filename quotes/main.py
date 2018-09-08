import asyncio
import bson.json_util
import json

from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URI = 'mongodb://test:test1234@localhost:27017'


@asyncio.coroutine
def setup_db():
    db = AsyncIOMotorClient(MONGO_URI).test
    yield from db.quotes.drop()
    with open('data.json') as f:
        data = json.load(f)

    yield from db.quotes.insert_many(data)
    yield from db.quotes.create_index([('author', 'text')])

    return db


@asyncio.coroutine
def author_handler(request):
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = yield from get_random_element(db.quotes, pipeline)
    return web.Response(body=bson.json_util.dumps(quote_json), content_type='application/json')


@asyncio.coroutine
def random_handler(request):
    db = request.app['db']
    quote_json = yield from get_random_element(db.quotes)
    return web.Response(body=bson.json_util.dumps(quote_json), content_type='application/json')


@asyncio.coroutine
def get_random_element(collection, pipeline=[]):
    random_element = {'$sample': {'size': 1}}
    pipeline.append(random_element)
    cursor = collection.aggregate(pipeline)
    while (yield from cursor.fetch_next):
        return cursor.next_object()
    return None


def main():
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(setup_db())
    app = web.Application()
    app['db'] = db
    app.router.add_get('/author/{author}', author_handler)
    app.router.add_get('/random', random_handler)
    web.run_app(app)

