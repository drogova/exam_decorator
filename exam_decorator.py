import functools
import logging
from unittest.mock import patch, call
import pytest
import time

LOGGER_FILENAME = 'function_logger.log'


@pytest.fixture()
def patcher():
    return patch('logging.debug')


@pytest.mark.parametrize('resp,exp', [
    (1, 2),
    (55, 56),
])
def test_function_result(resp, exp):
    assert timeit()(incr)(resp) == exp


@pytest.mark.parametrize('resp,exp', [
    (None, 'incr'),
    ('prefix', 'prefix'),
])
def test_debug_argument(resp, exp, patcher):
    with patcher as mo:
        timeit(resp)(incr)(5)
        calls = [
            call(f'{exp} started'),
            call(f'{exp} finished')
        ]
        mo.assert_has_calls(calls, any_order=True)


def timeit(prefix: str = None) -> int:
    """Function Logger"""
    def decorated(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logging.basicConfig(filename=LOGGER_FILENAME,
                                level=logging.DEBUG,
                                format='%(levelname)s: %(asctime)s – %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            prefix_logger = func.__name__ if prefix is None else prefix
            logging.debug(f'{prefix_logger} started')
            result = func(*args, **kwargs)
            logging.debug(f'{prefix_logger} finished')
            return result
        return wrapped
    return decorated


@timeit()
def incr(value: int) -> int:
    """Increase value by 1"""
    return value + 1


if __name__ == '__main__':
    incr(1)
    time.sleep(5)
    incr(10)
