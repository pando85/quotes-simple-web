from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import unittest

from quotes import main


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        return main.get_app()

    @unittest_run_loop
    async def test_example(self):
        request = await self.client.request("GET", "/quotes/random")
        assert request.status == 200
        text = await request.text()
        assert 'author' in text


if __name__ == '__main__':
    unittest.main()
