from celery import shared_task
from .models import Post


@shared_task
def publish_scheduled_posts():
    posts = Post.objects.filter(status="draft")

    for post in posts:
        # placeholder for future scheduling logic
        pass
