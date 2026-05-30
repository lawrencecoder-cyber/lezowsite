from apps.dashboard.widgets import WidgetRegistry
from apps.stocks.models import Stock


@WidgetRegistry.register("top_stocks")
class TopStocksWidget:

    def render(self):
        stocks = Stock.objects.all()[:10]
        return {
            "stocks": stocks
        }
