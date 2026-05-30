from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post

User = get_user_model()


class BlogTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="pass12345"
        )

    def test_create_post(self):
        post = Post.objects.create(
            author=self.user,
            title="Test Post",
            content="Hello world",
            status="published"
        )

        self.assertEqual(post.slug, "test-post")
        self.assertEqual(post.author.username, "tester")
