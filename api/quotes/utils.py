from typing import Any, TypeVar, Optional, Callable

from quotes.quote import Quote

T = TypeVar('T')


def compose(*funcs: Any) -> Callable:
    first, second, *rest = funcs
    if rest:
        second = compose(second, *rest)
    return lambda *args, **kwargs: second(first(*args, **kwargs))


def bind(f: Callable, x: Optional[T]) -> Optional[T]:
    if x is None:
        return None
    return f(x)


def dict_to_quote(_dict: dict) -> Quote:
    quote_json = {'author': _dict['author'],
                  'quote': _dict['quote']}
    return Quote(**quote_json)
