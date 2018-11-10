import asyncio
import functools
import unittest

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from quotes.app import get_app
from quotes.db import get_random_quote, setup_db


class DBTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app(setup_db)

    @unittest_run_loop
    async def test_get_random_quote(self):
        total_queries = 1000
        success_rate = 0.1
        range_rate = 0.03
        example_quote = 'UNIX is basically a simple operating system, but you have ' \
            'to be a genius to understand the simplicity.'
        random_quote_generator = [
            get_random_quote(self) for _ in range(1, total_queries)]

        random_quote_list = await asyncio.gather(*random_quote_generator)
        results_list = [
            1 if random_quote.quote == example_quote else 0
            for random_quote in random_quote_list]

        def sum(x, y):
            return x + y
        result_success = functools.reduce(sum, results_list)
        result_success_rate = result_success / total_queries

        assert (result_success_rate > success_rate - range_rate)
        assert (result_success_rate < success_rate + range_rate)


if __name__ == '__main__':
    unittest.main()
