from .models import Post


class PostSelector:
    @staticmethod
    def published_posts():
        return Post.objects.filter(status="published")

    @staticmethod
    def post_by_slug(slug):
        return Post.objects.filter(slug=slug, status="published").first()

    @staticmethod
    def user_posts(user):
        return Post.objects.filter(author=user)


class BlogSelector:

    @staticmethod
    def published_posts():
        return Post.published.all().order_by("-created_at")

    @staticmethod
    def get_post_by_slug(slug):
        return Post.objects.filter(slug=slug).first()
