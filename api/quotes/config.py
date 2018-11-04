import os


MONGO_USER: str = os.environ.get('MONGO_USER', 'test')
MONGO_PASSWORD: str = os.environ.get('MONGO_PASSWORD', 'test1234')
MONGO_URI: str = os.environ.get(
    'MONGO_URI', f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017')

DATA_PATH: str = os.environ.get('DATA_PATH', 'data')
QUOTES_FILE_PATH: str = os.environ.get('QUOTES_FILE_PATH', f'{DATA_PATH}/quotes.json')
AUDIO_DIR_PATH: str = os.environ.get('AUDIO_DIR_PATH', f'{DATA_PATH}/audio')

IS_CREATE_EMPTY_AUDIO_FILES: bool = os.environ.get(
    'IS_CREATE_EMPTY_AUDIO_FILES', 'False').lower() == 'true'

CORS_ALLOW_ORIGIN: str = os.environ.get('CORS_ALLOW_ORIGIN', '*')

LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')
