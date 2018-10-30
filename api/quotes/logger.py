import logging
import sys

from quotes.config import LOG_LEVEL


logger = logging.getLogger('')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.getLevelName(LOG_LEVEL))
console_handler.setFormatter(logging.Formatter('-- %(levelname)s -- %(message)s'))
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)
