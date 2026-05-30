from .finnhub import FinnhubClient
from ..models import Stock


class MarketDataService:
    def __init__(self):
        self.client = FinnhubClient()

    def update_stock(self, stock: Stock):
        data = self.client.get_quote(stock.symbol)

        if not data:
            return stock

        stock.previous_close = data.get("pc", 0)
        stock.current_price = data.get("c", 0)

        stock.change = stock.current_price - stock.previous_close

        if stock.previous_close:
            stock.percent_change = (
                stock.change / stock.previous_close
            ) * 100

        stock.save()
        return stock

    def bulk_update(self):
        stocks = Stock.objects.all()

        return [self.update_stock(stock) for stock in stocks]
