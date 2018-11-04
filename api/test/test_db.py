import asyncio
import functools
import json
import os
import unittest

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from quotes.app import get_app
from quotes.config import QUOTES_FILE_PATH, AUDIO_DIR_PATH
from quotes.db import load_db, mongo_connection, get_random_element
from quotes.utils import add_audio_to_json


async def setup_db_test(app):
    await mongo_connection(app)
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    test_quotes_file_path = os.path.join(current_file_path, QUOTES_FILE_PATH)
    await load_db(app, test_quotes_file_path)
    test_audio_dir_path = os.path.join(current_file_path, AUDIO_DIR_PATH)
    await add_audio_to_json(app['db'], test_audio_dir_path)


class DBTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app(setup_db_test)

    @unittest_run_loop
    async def test_get_random_element(self):
        total_queries = 1000
        success_rate = 0.1
        range_rate = 0.03
        example_quote = 'UNIX is basically a simple operating system, but you have ' \
            'to be a genius to understand the simplicity.'
        random_quote_generator = [
            get_random_element(self.app['db'].quotes) for _ in range(1, total_queries)]

        random_quote_list = await asyncio.gather(*random_quote_generator)
        results_list = [
            1 if random_quote.quote == example_quote else 0
            for random_quote in random_quote_list]

        def sum(x, y):
            return x + y
        result_success = functools.reduce(sum, results_list)
        result_success_rate = result_success / total_queries
        assert (result_success_rate > success_rate - result_success_rate * range_rate)
        assert (result_success_rate < success_rate + result_success_rate * range_rate)


if __name__ == '__main__':
    unittest.main()
