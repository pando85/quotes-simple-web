import aiohttp.web
import aiohttp_cors
from typing import Awaitable, Callable

from quotes.handlers import random_handler, ping_handler
from quotes.config import AUDIO_ENDPOINT, AUDIOS_PATH, CORS_ALLOW_ORIGIN


def get_app(setup_db: Callable[[aiohttp.web.Application], Awaitable[None]]
            ) -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.add_routes([
        aiohttp.web.get('/ping', ping_handler),
        aiohttp.web.get('/quotes/random', random_handler),
        aiohttp.web.static(AUDIO_ENDPOINT, AUDIOS_PATH)
    ])

    cors = aiohttp_cors.setup(app, defaults={
        CORS_ALLOW_ORIGIN: aiohttp_cors.ResourceOptions(),
    })
    [cors.add(route) for route in list(app.router.routes())]

    return app
