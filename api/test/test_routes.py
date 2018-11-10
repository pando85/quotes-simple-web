from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import unittest

from quotes.app import get_app
from quotes.db import setup_db


class RoutesTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app(setup_db)

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
