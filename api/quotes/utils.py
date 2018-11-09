from typing import Any, TypeVar, Optional, Callable

from quotes.quote import Quote

T = TypeVar('T')


def compose(*funcs: Any) -> Callable:
    *rest, penultimate, last = funcs
    if rest:
        penultimate = compose(*rest, penultimate)
    return lambda *args, **kwargs: penultimate(last(*args, **kwargs))


def bind(f: Callable, x: Optional[T]) -> Optional[T]:
    if x is None:
        return None
    return f(x)


def dict_to_quote(_dict: dict) -> Quote:
    quote_json = {'author': _dict['author'],
                  'quote': _dict['quote']}
    return Quote(**quote_json)
