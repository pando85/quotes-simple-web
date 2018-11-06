import logging
import sys

from quotes.config import LOG_LEVEL


logger = logging.getLogger(__name__)
logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(LOG_LEVEL)
logger_handler.setFormatter(
    logging.Formatter('-- %(levelname)s -- %(asctime)s -- %(filename)s -- %(message)s'))
logger.addHandler(logger_handler)
logger.setLevel(LOG_LEVEL)

access_logger = logging.getLogger('aiohttp.access')
access_handler = logging.StreamHandler(sys.stdout)
access_handler.setLevel(LOG_LEVEL)
access_logger.addHandler(access_handler)
access_logger.setLevel(LOG_LEVEL)
