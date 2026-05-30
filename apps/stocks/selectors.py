from .models import Stock


class StockSelector:

    @staticmethod
    def all_stocks():
        return Stock.objects.all()

    @staticmethod
    def get_stock(symbol):
        return Stock.objects.filter(symbol=symbol).first()
