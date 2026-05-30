from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="pass1234"
        )

        self.assertEqual(user.username, "test")
