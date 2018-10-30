import logging
import sys

from quotes.config import LOG_LEVEL


def get_logger():
    logger = logging.getLogger('')
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.getLevelName(LOG_LEVEL))
    logger.addHandler(stdout_handler)
    logger.setLevel(LOG_LEVEL)

    return logger
