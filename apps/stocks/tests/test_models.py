from django.test import TestCase
from ..models import Stock


class StockModelTest(TestCase):

    def test_stock_creation(self):
        stock = Stock.objects.create(
            symbol="AAPL",
            name="Apple Inc"
        )

        self.assertEqual(stock.symbol, "AAPL")
