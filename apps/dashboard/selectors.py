from apps.stocks.models import Stock


class DashboardSelector:

    @staticmethod
    def get_top_stocks(limit=20):
        return Stock.objects.all().order_by("-current_price")[:limit]

    @staticmethod
    def get_movers():
        return Stock.objects.order_by("-percent_change")[:10]
