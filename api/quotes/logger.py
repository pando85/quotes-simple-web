import logging
from typing import TypeVar
import sys

from quotes.config import LOG_LEVEL

T = TypeVar('T')


logger = logging.getLogger(__name__)
logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(LOG_LEVEL)
logger_handler.setFormatter(
    logging.Formatter('%(levelname)s - %(asctime)s - %(message)s'))
logger.addHandler(logger_handler)
logger.setLevel(LOG_LEVEL)

access_logger = logging.getLogger('aiohttp.access')
access_handler = logging.StreamHandler(sys.stdout)
access_handler.setLevel(LOG_LEVEL)
access_logger.addHandler(access_handler)
access_logger.setLevel(LOG_LEVEL)


def critical(x: T) -> T:
    logger.critical(x)
    return x


def error(x: T) -> T:
    logger.error(x)
    return x


def warning(x: T) -> T:
    logger.warning(x)
    return x


def info(x: T) -> T:
    logger.info(x)
    return x


def debug(x: T) -> T:
    logger.debug(x)
    return x
