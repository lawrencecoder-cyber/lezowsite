from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsTestCase(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="strongpassword123"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("strongpassword123"))
