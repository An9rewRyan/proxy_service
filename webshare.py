import logging
import random
import time
from functools import wraps
from typing import Optional, List
import requests

logger = logging.getLogger(__name__)


def wait_success_response(timeout: float = 60):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time.time()
            while time.time() < start_time + timeout:
                try:
                    result = func(*args, **kwargs)
                    if result is not None:
                        return result
                except Exception as e:
                    logger.error(f'Some error in {func.__qualname__}: {e}')
                delay: float = random.uniform(1, 5)
                time.sleep(delay)
            logger.info(f'{func.__qualname__} exited on timeout {timeout} sec')

        return wrapped

    return decorator


class Updator:
    """
    Датацентр прокси.
    Доступные регионы: [BE, ES, IL, NO, US, CZ, FI, IT, RU, DE, FR, NL, UA].
    """
    _API_KEY = '3q3dxfbsocl90tfc2mnkzvrx70wt84d7sq23yd64'
    _AUTH_HEADERS = {'Authorization': f'Token {_API_KEY}'}
    # с API не приходит более 100 прокси за раз даже если page_size больше 100
    _PROXIES_API_URL = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page_size=100"

    def load_proxies(self):
        api_url = self._PROXIES_API_URL
        proxies = []
        while api_url:
            response = self._get_proxies_from_api(api_url) or {}
            proxies.extend(response.get('results', []))
            api_url = response.get('next')

        return proxies

    @wait_success_response(timeout=120)
    def _get_proxies_from_api(self, api_url: str) -> Optional[List[dict]]:
        response = requests.get(api_url, headers=self._AUTH_HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json()


# if __name__ == "main":
# updator = Updator()
# proxies = updator.load_proxies()
# print(proxies)
