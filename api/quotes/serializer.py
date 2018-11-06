import json
from typing import Optional

from quotes.quote import Quote


def quote_to_json(quote: Optional[Quote]) -> str:
    if not quote:
        return "{'error': 'Not quote found'}"
    return json.dumps({'author': quote.author, 'quote': quote.quote}, ensure_ascii=False)
