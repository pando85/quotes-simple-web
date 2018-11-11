import pathlib
import json

from quotes.config import AUDIO_ENDPOINT, QUOTES_AUTHOR
from quotes.quote import Quote
from quotes import logger


def dict_from_transcript(transcript: dict) -> dict:
    quote_json = {'audio': f'{AUDIO_ENDPOINT}/{transcript["jobName"]}',
                  'author': QUOTES_AUTHOR,
                  'quote': transcript['results']['transcripts'][0]['transcript']}
    return quote_json


def quote_from_dict(_dict: dict) -> Quote:
    quote_json = {'audio': _dict['audio'],
                  'author': _dict['author'],
                  'quote': _dict['quote']}
    return Quote(**quote_json)


def list_files_in_directory(path):
    p = pathlib.Path(path).glob('**/*')
    return [x for x in p if x.is_file()]


def read_file(path):
    logger.debug(f'Reading file `{path}` ...')
    with open(path) as f:
        data = json.load(f)
    return data
