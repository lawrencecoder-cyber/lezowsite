from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock
from .services.websocket import StockWebSocketService


@receiver(post_save, sender=Stock)
def stock_updated(sender, instance, **kwargs):
    StockWebSocketService.push_update(instance)
