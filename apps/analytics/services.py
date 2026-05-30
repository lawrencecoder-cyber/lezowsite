import statistics
from apps.analytics.models import StockSnapshot


class AnalyticsService:

    @staticmethod
    def record_snapshot(stock):
        return StockSnapshot.objects.create(
            stock=stock,
            price=stock.current_price,
            change=stock.change,
            percent_change=stock.percent_change,
        )

    @staticmethod
    def calculate_volatility(symbol):
        snapshots = StockSnapshot.objects.filter(
            stock__symbol=symbol
        ).values_list("percent_change", flat=True)

        if len(snapshots) < 2:
            return 0

        return statistics.pstdev(snapshots)
