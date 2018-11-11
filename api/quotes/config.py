import os


MONGO_USER: str = os.environ.get('MONGO_USER', 'test')
MONGO_PASSWORD: str = os.environ.get('MONGO_PASSWORD', 'test1234')
MONGO_URI: str = os.environ.get(
    'MONGO_URI', f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017')

DATA_PATH: str = os.environ.get('DATA_PATH', 'test/data')
AUDIOS_PATH: str = os.environ.get('AUDIOS_PATH', f'{DATA_PATH}/audios')
QUOTES_PATH: str = os.environ.get('QUOTES_PATH', f'{DATA_PATH}/transcripts')

QUOTES_AUTHOR: str = os.environ.get('QUOTES_AUTHOR', 'Unknown')

CORS_ALLOW_ORIGIN: str = os.environ.get('CORS_ALLOW_ORIGIN', '*')

LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')
