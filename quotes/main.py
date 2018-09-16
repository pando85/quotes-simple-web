import aiohttp.web
import asyncio


from quotes.app import get_app
from quotes.db import setup_db


def main():
    app = get_app(setup_db)
    aiohttp.web.run_app(app)
