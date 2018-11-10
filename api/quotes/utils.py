from quotes.quote import Quote


def dict_to_quote(_dict: dict) -> Quote:
    quote_json = {'author': _dict['author'],
                  'quote': _dict['quote']}
    return Quote(**quote_json)
