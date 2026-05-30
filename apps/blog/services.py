from datetime import datetime
from .models import Post


class PostService:
    @staticmethod
    def create_post(form, user):
        post = form.save(commit=False)
        post.author = user

        if post.status == Post.Status.PUBLISHED:
            post.published_at = datetime.now()

        post.save()
        return post

    @staticmethod
    def update_post(post, form):
        updated = form.save(commit=False)

        if updated.status == Post.Status.PUBLISHED and not post.published_at:
            updated.published_at = datetime.now()

        updated.save()
        return updated

class BlogService:

    @staticmethod
    def create_post(user, title, content, tags=""):
        return Post.objects.create(
            author=user,
            title=title,
            content=content,
            tags=tags,
            status="draft"
        )

    @staticmethod
    def publish_post(post):
        post.status = "published"
        post.save()
