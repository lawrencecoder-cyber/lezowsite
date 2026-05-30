from django.core.cache import cache


class CacheService:

    @staticmethod
    def set(key, value, timeout=60):
        cache.set(key, value, timeout)

    @staticmethod
    def get(key):
        return cache.get(key)

    @staticmethod
    def delete(key):
        cache.delete(key)
