import os


DATA_PATH: str = os.environ.get('DATA_PATH', 'test/data')
AUDIOS_PATH: str = os.environ.get('AUDIOS_PATH', f'{DATA_PATH}/audios')
QUOTES_PATH: str = os.environ.get('QUOTES_PATH', f'{DATA_PATH}/transcripts')

AUDIO_ENDPOINT: str = os.environ.get('AUDIO_ENDPOINT', '/audio')
QUOTES_AUTHOR: str = os.environ.get('QUOTES_AUTHOR', 'Unknown')
QUOTES_AUDIO_KEY: str = os.environ.get('QUOTES_AUDIO_KEY', '["audio"]')
QUOTES_TRANSCRIPT_KEY: str = os.environ.get(
    'QUOTES_TRANSCRIPT_KEY', '["transcript"]')


CORS_ALLOW_ORIGIN: str = os.environ.get('CORS_ALLOW_ORIGIN', '*')

LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')
