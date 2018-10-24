import aiohttp.web

from quotes.handlers import author_handler, random_handler


def get_app(setup_db):
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.add_routes([
        aiohttp.web.get('/quotes/random', random_handler),
        aiohttp.web.get('/quotes/random/{author}', author_handler)
    ])
    return app
