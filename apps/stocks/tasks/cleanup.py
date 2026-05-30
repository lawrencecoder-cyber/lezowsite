from celery import shared_task
from django.core.cache import cache


@shared_task
def clear_stock_cache():
    cache.clear()
