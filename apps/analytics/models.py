from django.db import models
from django.conf import settings
from apps.stocks.models import Stock


class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    metadata = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)


class StockSnapshot(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=12, decimal_places=2)
    change = models.DecimalField(max_digits=12, decimal_places=2)
    percent_change = models.DecimalField(max_digits=6, decimal_places=2)

    recorded_at = models.DateTimeField(auto_now_add=True)


class MarketSummary(models.Model):
    symbol = models.CharField(max_length=10)

    avg_price = models.DecimalField(max_digits=12, decimal_places=2)
    avg_change = models.DecimalField(max_digits=12, decimal_places=2)
    volatility = models.DecimalField(max_digits=10, decimal_places=4)

    period = models.CharField(max_length=20, default="daily")
    created_at = models.DateTimeField(auto_now_add=True)
