import os


MONGO_USER = os.environ.get('MONGO_USER', 'test')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'test1234')
MONGO_URI = os.environ.get('MONGO_URI', f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017')

QUOTES_FILE_PATH = os.environ.get('QUOTES_FILE_PATH', 'data/quotes.json')
