from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Watchlist
from apps.notifications.services import send_notification


@receiver(post_save, sender=Watchlist)
def watchlist_created(sender, instance, created, **kwargs):
    if created:
        send_notification(
            instance.user,
            f"Watchlist '{instance.name}' created successfully"
        )
