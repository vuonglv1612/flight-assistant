import logging
import time
from functools import wraps
from typing import Tuple, Type

logger = logging.getLogger(__name__)


def retry(
    max_attempt: int, delay: int, exceptions: Tuple[Type[Exception]] = (Exception,)
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempt):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt < max_attempt - 1:
                        logger.warning(
                            (
                                "Attempt %s/%s failed,"
                                " retrying function %s in %s seconds"
                            ),
                            attempt,
                            max_attempt,
                            func.__name__,
                            delay,
                        )
                        time.sleep(delay)
                    else:
                        raise

        return wrapper

    return decorator
