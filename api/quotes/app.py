import aiohttp.web
import aiohttp_cors
from typing import Awaitable, Callable

from quotes.handlers import author_handler, random_handler
from quotes.config import CORS_ALLOW_ORIGIN


def get_app(setup_db: Callable[[aiohttp.web.Application], Awaitable[None]]
            ) -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.add_routes([
        aiohttp.web.get('/quotes/random', random_handler),
        aiohttp.web.get('/quotes/random/{author}', author_handler)
    ])

    cors = aiohttp_cors.setup(app, defaults={
        CORS_ALLOW_ORIGIN: aiohttp_cors.ResourceOptions(),
    })
    [cors.add(route) for route in list(app.router.routes())]

    return app
