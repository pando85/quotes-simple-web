import json
from functools import partial

from quotes.quote import Quote
from quotes.functools import bind


def _quote_to_json(quote: Quote) -> str:
    return json.dumps({'author': quote.author, 'quote': quote.quote}, ensure_ascii=False)


quote_to_json = partial(bind, _quote_to_json)
