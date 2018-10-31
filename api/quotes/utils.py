import os
import pathlib
from typing import List

from quotes.config import AUDIO_DIR_PATH, IS_CREATE_EMPTY_AUDIO_FILES


def _list_files_in_directory(path: str) -> List[pathlib.Path]:
    p = pathlib.Path(path).glob('**/*')
    return [x for x in p if x.is_file()]


def _create_file(path):
    return open(path, 'a').close()


async def add_audio_to_json(db, path):
    files = _list_files_in_directory(AUDIO_DIR_PATH)
    filenames = map(os.path.basename, files)
    if not filenames:
        return
    search_queries = map(lambda x: '.'.join(x.split('.')[0:-1]), filenames)

    if IS_CREATE_EMPTY_AUDIO_FILES:
        # for author in authors
        all_quotes_cursor = db.quotes.find({'author': 'Mariano Rajoy'}, {'quote': 1})
        while(await all_quotes_cursor.fetch_next):
            quote = all_quotes_cursor.next_object()
            try:
                query_path = f'data/audio/Mariano Rajoy/{quote["quote"]}.mp3'
                _create_file(query_path)
            except FileExistsError:
                continue

    for path in search_queries:
        await db.quotes.update_many(
            {'quote': path},
            {'$set': {'audio_path': f'{AUDIO_DIR_PATH}/{path}.mp3'}})
