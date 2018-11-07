from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import os
import unittest

from quotes.app import get_app
from quotes.config import QUOTES_FILE_PATH
from quotes.db import load_db, mongo_connection


async def setup_db_test(app):
    await mongo_connection(app)
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    test_quotes_file_path = os.path.join(current_file_path, QUOTES_FILE_PATH)
    await load_db(app, test_quotes_file_path)


class RoutesTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app(setup_db_test)

    @unittest_run_loop
    async def test_ping(self, url='/ping'):
        request = await self.client.request('GET', url)
        assert request.status == 200
        response = await request.json()
        assert response == 'pong'

    @unittest_run_loop
    async def test_random_handler(self, url='/quotes/random'):
        request = await self.client.request('GET', url)
        assert request.status == 200
        quote = await request.json()
        assert ('author' and 'quote') in quote

    def test_get_author_random_handler(self):
        self.test_random_handler('/quotes/random/dennis%20ritchie')

    @unittest_run_loop
    async def test_fail_author_random_handler(self):
        request = await self.client.request('GET', '/quotes/random/failauthorsearch')
        assert request.status == 500


if __name__ == '__main__':
    unittest.main()
