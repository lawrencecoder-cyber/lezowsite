from celery import shared_task
import requests
from django.conf import settings


@shared_task
def fetch_market_news():
    url = "https://finnhub.io/api/v1/news"

    response = requests.get(
        url,
        params={
            "category": "general",
            "token": settings.FINNHUB_API_KEY,
        },
        timeout=10,
    )

    return response.json()
