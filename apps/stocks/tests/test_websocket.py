from django.test import TestCase
from apps.stocks.websocket.handlers import StockEventHandler


class WebSocketTest(TestCase):

    def test_price_event(self):
        class MockStock:
            symbol = "AAPL"
            current_price = 100
            change = 2
            percent_change = 1.5

        event = StockEventHandler.handle_price_update(MockStock)

        self.assertEqual(event["type"], "stock.price_update")
