from celery import shared_task
from .update_prices import update_all_stock_prices
from .update_market_news import fetch_market_news


@shared_task
def run_stock_pipeline():
    update_all_stock_prices.delay()
    fetch_market_news.delay()
