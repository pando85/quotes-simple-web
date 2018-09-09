import aiohttp.web
import asyncio
import json
import pymongo

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URI = 'mongodb://test:test1234@localhost:27017'


async def mongo_connection(app):
    mongo = AsyncIOMotorClient(MONGO_URI)
    async def cleanup(app):
        mongo.close()
    app.on_cleanup.append(cleanup)
    app['db'] = mongo['test']


async def load_db(app, path):
    await app['db'].quotes.drop()
    with open(path) as f:
        data = json.load(f)
    await app['db'].quotes.insert_many(data)
    await app['db'].quotes.create_index([('author', pymongo.TEXT)])


async def setup_db(app):
    await mongo_connection(app)
    await load_db(app, 'data.json')


async def author_handler(request):
    db = request.app['db']
    author = request.match_info['author']
    pipeline = [{'$match': {'$text': {'$search': author}}}]
    quote_json = await get_random_element(db.quotes, pipeline)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')


def json_dump(response_json):
    if '_id' in response_json:
        del response_json['_id']
    return json.dumps(response_json, ensure_ascii=False)


async def random_handler(request):
    db = request.app['db']
    quote_json = await get_random_element(db.quotes)
    return aiohttp.web.Response(body=json_dump(quote_json), content_type='application/json')


async def get_random_element(collection, pipeline=[]):
    random_element = {'$sample': {'size': 1}}
    pipeline.append(random_element)
    cursor = collection.aggregate(pipeline)
    while (await cursor.fetch_next):
        return cursor.next_object()
    raise aiohttp.web.HTTPNotFound()


def get_app(setup_db):
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.router.add_get('/quotes/random', random_handler)
    app.router.add_get('/quotes/random/{author}', author_handler)
    return app


def main():
    app = get_app(setup_db)
    aiohttp.web.run_app(app)
