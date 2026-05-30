from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from apps.analytics.trackers import ActivityTracker

@receiver(pre_save, sender=Post)
def ensure_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance.title.lower().replace(" ", "-")


@receiver(post_save, sender=Post)
def track_post_creation(sender, instance, created, **kwargs):
    if created:
        ActivityTracker.track(
            instance.author,
            "create_post",
            {"post_id": instance.id}
        )
