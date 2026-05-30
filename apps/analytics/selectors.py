from .models import UserActivity, StockSnapshot, MarketSummary


class AnalyticsSelector:

    @staticmethod
    def user_activity(user):
        return UserActivity.objects.filter(user=user).order_by("-created_at")

    @staticmethod
    def stock_history(symbol):
        return StockSnapshot.objects.filter(
            stock__symbol=symbol
        ).order_by("-recorded_at")

    @staticmethod
    def market_summaries():
        return MarketSummary.objects.all()
