import os


MONGO_USER = os.environ.get('MONGO_USER', 'test')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'test1234')
MONGO_URI = os.environ.get('MONGO_URI', f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017')

DATA_PATH = os.environ.get('DATA_PATH', 'data')
QUOTES_FILE_PATH = os.environ.get('QUOTES_FILE_PATH', f'{DATA_PATH}/quotes.json')
AUDIO_DIR_PATH = os.environ.get('AUDIO_DIR_PATH', f'{DATA_PATH}/audio')

IS_CREATE_EMPTY_AUDIO_FILES = os.environ.get('IS_CREATE_EMPTY_AUDIO_FILES', False)

CORS_ALLOW_ORIGIN = os.environ.get('CORS_ALLOW_ORIGIN', '*')

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
