from celery import shared_task
from apps.stocks.models import Stock
from apps.analytics.services import AnalyticsService
from .models import MarketSummary
import statistics


@shared_task
def generate_stock_snapshots():
    stocks = Stock.objects.all()

    for stock in stocks:
        AnalyticsService.record_snapshot(stock)


@shared_task
def compute_market_summary():
    stocks = Stock.objects.all()

    for stock in stocks:
        snapshots = stock.stocksnapshot_set.all()

        if not snapshots:
            continue

        prices = [s.price for s in snapshots]

        summary, _ = MarketSummary.objects.get_or_create(
            symbol=stock.symbol
        )

        summary.avg_price = sum(prices) / len(prices)
        summary.avg_change = sum([s.change for s in snapshots]) / len(snapshots)

        summary.volatility = statistics.pstdev(prices) if len(prices) > 1 else 0

        summary.save()

