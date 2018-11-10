from typing import Any, Callable,  Optional, TypeVar

T = TypeVar('T')


def bind(f: Callable, x: Optional[T]) -> Any:
    if x is None:
        return None
    return f(x)
