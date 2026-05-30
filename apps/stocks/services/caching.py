from django.core.cache import cache


class StockCache:
    @staticmethod
    def set(symbol, data):
        cache.set(f"stock:{symbol}", data, timeout=30)

    @staticmethod
    def get(symbol):
        return cache.get(f"stock:{symbol}")
