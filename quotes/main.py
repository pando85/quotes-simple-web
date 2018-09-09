import aiohttp.web
import asyncio
import json
import pymongo

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URI = 'mongodb://test:test1234@localhost:27017'


def setup_db(app, loop=None):
    mongo = AsyncIOMotorClient(MONGO_URI, io_loop=loop)
    db = mongo['test']
    async def cleanup(app):
        mongo.close()
    app.on_cleanup.append(cleanup)
    return db


def initialize_db(db):
    yield from db.quotes.drop()
    with open('data.json') as f:
        data = json.load(f)
    print(data)
    yield from db.quotes.insert_many(data)
    yield from db.quotes.create_index([('author', pymongo.TEXT)])
    return db


@asyncio.coroutine
def author_handler(request):
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = yield from get_random_element(db.quotes, pipeline)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')


def json_dump(response_json):
    if '_id' in response_json:
        del response_json['_id']
    return json.dumps(response_json, ensure_ascii=False)


@asyncio.coroutine
def random_handler(request):
    db = request.app['db']
    quote_json = yield from get_random_element(db.quotes)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')


@asyncio.coroutine
def get_random_element(collection, pipeline=[]):
    random_element = {'$sample': {'size': 1}}
    pipeline.append(random_element)
    cursor = collection.aggregate(pipeline)
    while (yield from cursor.fetch_next):
        return cursor.next_object()
    raise aiohttp.web.HTTPNotFound()


def get_app():
    loop = asyncio.get_event_loop()
    app = aiohttp.web.Application(loop=loop)
    app['db'] = setup_db(app, loop)
    app.router.add_get('/quotes/random', random_handler)
    app.router.add_get('/quotes/random/{author}', author_handler)
    return app


def main():
    app = get_app(loop)
    loop.run_until_complete(initialize_db(app['db']))
    aiohttp.web.run_app(app)
