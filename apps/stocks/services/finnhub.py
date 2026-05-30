import requests
from django.conf import settings
from django.core.cache import cache
from apps.stocks.constants import FINNHUB_BASE_URL, CACHE_TTL


class FinnhubClient:
    def __init__(self):
        self.api_key = settings.FINNHUB_API_KEY

    def get_quote(self, symbol: str):
        cache_key = f"quote:{symbol}"

        cached = cache.get(cache_key)
        if cached:
            return cached

        try:
            response = requests.get(
                f"{FINNHUB_BASE_URL}/quote",
                params={
                    "symbol": symbol,
                    "token": self.api_key,
                },
                timeout=8,
            )
            response.raise_for_status()

            data = response.json()

            cache.set(cache_key, data, CACHE_TTL)

            return data

        except requests.RequestException:
            return None
