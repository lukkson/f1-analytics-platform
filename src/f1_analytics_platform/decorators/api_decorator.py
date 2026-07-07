import functools
import logging

import requests

from f1_analytics_platform.exceptions import (
    F1ApiException,
    F1ApiConnectionException,
    F1ApiNotFoundException,
)

logger = logging.getLogger(__name__)


def handle_api_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError as e:
            logger.error(e)
            raise F1ApiConnectionException(f"Connection error: {e}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.error(e)
                raise F1ApiNotFoundException(
                    f"Resource not found: {e.response.url} returned {e.response.status_code}"
                )
            logger.error(e)
            raise F1ApiException(f"Unexpected error: {e}")
        except Exception as e:
            logger.error(e)
            raise F1ApiException(f"Unexpected error: {e}")

    return wrapper
