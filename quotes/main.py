import aiohttp.web
import asyncio
import json
import pymongo

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URI = 'mongodb://test:test1234@localhost:27017'


async def setup_db(app):
    mongo = AsyncIOMotorClient(MONGO_URI)
    async def cleanup(app):
        mongo.close()
    app.on_cleanup.append(cleanup)
    app['db'] = mongo['test']
    await load_db(app)


async def load_db(app):
    await app['db'].quotes.drop()
    with open('data.json') as f:
        data = json.load(f)
    await app['db'].quotes.insert_many(data)
    await app['db'].quotes.create_index([('author', pymongo.TEXT)])


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
    app.on_startup.append(setup_db)
    app.router.add_get('/quotes/random', random_handler)
    app.router.add_get('/quotes/random/{author}', author_handler)
    return app


def main():
    app = get_app()
    aiohttp.web.run_app(app)
