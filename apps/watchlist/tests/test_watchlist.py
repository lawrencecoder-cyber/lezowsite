from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Watchlist

User = get_user_model()


class WatchlistTest(TestCase):

    def test_watchlist_creation(self):
        user = User.objects.create_user(
            username="tester",
            password="pass123"
        )

        wl = Watchlist.objects.create(user=user, name="Tech Stocks")

        self.assertEqual(wl.name, "Tech Stocks")
