import aiohttp.web

from quotes.app import get_app
from quotes.db import setup_db
from quotes.logger import access_logger


def main():
    app = get_app(setup_db)
    aiohttp.web.run_app(app, access_log=access_logger)
