from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import unittest
import os

from quotes import main


async def setup_db_test(app):
    await main.mongo_connection(app)
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    test_data_path = os.path.join(current_file_path, 'data.json')
    await main.load_db(app, test_data_path)


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        return main.get_app(setup_db_test)

    @unittest_run_loop
    async def test_example(self):
        request = await self.client.request("GET", "/quotes/random")
        assert request.status == 200
        text = await request.text()
        assert 'author' in text


if __name__ == '__main__':
    unittest.main()
