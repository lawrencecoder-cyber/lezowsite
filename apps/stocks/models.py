from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)

    exchange = models.CharField(max_length=50, blank=True)

    current_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    previous_close = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    change = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    percent_change = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol
