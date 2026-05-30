from django.test import TestCase
from ..services import AnalyticsService
from apps.stocks.models import Stock


class AnalyticsTest(TestCase):

    def test_snapshot_creation(self):
        stock = Stock.objects.create(symbol="AAPL", name="Apple")

        snapshot = AnalyticsService.record_snapshot(stock)

        self.assertEqual(snapshot.stock.symbol, "AAPL")
