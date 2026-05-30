from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PriceAlert
from .services import NotificationService


@receiver(post_save, sender=PriceAlert)
def alert_created(sender, instance, created, **kwargs):
    if created:
        NotificationService.create_notification(
            instance.user,
            f"Alert set for {instance.stock.symbol} at {instance.target_price}"
        )
