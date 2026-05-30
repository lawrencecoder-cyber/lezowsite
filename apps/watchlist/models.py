from django.db import models
from django.conf import settings
from apps.stocks.models import Stock


class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="watchlists",
    )
    name = models.CharField(max_length=100, default="My Watchlist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class WatchlistItem(models.Model):
    watchlist = models.ForeignKey(
        Watchlist,
        on_delete=models.CASCADE,
        related_name="items",
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("watchlist", "stock")
