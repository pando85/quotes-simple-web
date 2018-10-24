import aiohttp.web

from quotes.handlers import author_handler, random_handler


def get_app(setup_db):
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.router.add_get('/quotes/random', random_handler)
    app.router.add_get('/quotes/random/{author}', author_handler)
    return app
