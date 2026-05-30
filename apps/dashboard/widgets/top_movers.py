from apps.dashboard.widgets import WidgetRegistry
from apps.stocks.models import Stock


@WidgetRegistry.register("top_movers")
class TopMoversWidget:

    def render(self):
        stocks = Stock.objects.order_by("-percent_change")[:5]
        return {
            "stocks": stocks
        }
