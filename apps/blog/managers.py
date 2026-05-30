from django.db import models


class PostManager(models.Manager):
    def published(self):
        return self.filter(status="published")

    def drafts(self):
        return self.filter(status="draft")

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status="published")
