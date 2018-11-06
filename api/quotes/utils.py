import pathlib
from typing import List

from quotes.quote import Quote


def _list_files_in_directory(path: str) -> List[pathlib.Path]:
    p = pathlib.Path(path).glob('**/*')
    return [x for x in p if x.is_file()]


def _create_file(path: str) -> None:
    return open(path, 'a').close()


def dict_to_quote(_dict: dict) -> Quote:
    quote_json = {'author': _dict['author'],
                  'quote': _dict['quote']}
    return Quote(**quote_json)
