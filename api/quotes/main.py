import aiohttp.web
import asyncio


from quotes.app import get_app
from quotes.db import setup_db
from quotes.logger import get_logger


def main():
    app = get_app(setup_db)
    logger = get_logger()
    aiohttp.web.run_app(app, access_log=logger)
