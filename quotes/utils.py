import os
import pathlib

from quotes.config import AUDIO_DIR_PATH


def _list_files_in_directory(path):
    p = pathlib.Path(path).glob('**/*')
    return [x for x in p if x.is_file()]


async def add_audio_to_json(db, path):
    files = _list_files_in_directory(AUDIO_DIR_PATH)
    filenames = map(os.path.basename, files)
    if not filenames:
        return
    search_queries = map(lambda x: '.'.join(x.split('.')[0:-1]), filenames)
    for query in search_queries:
        await db.quotes.update_many({'quote': query}, {'$set': {'audio_path': query}})
