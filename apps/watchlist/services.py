from .models import Watchlist, WatchlistItem
from apps.stocks.models import Stock
from apps.notifications.channels import NotificationChannel

class WatchlistService:

    @staticmethod
    def create_watchlist(user, name="My Watchlist"):
        return Watchlist.objects.create(user=user, name=name)

    @staticmethod
    def add_stock(watchlist, symbol):
        stock = Stock.objects.filter(symbol=symbol).first()
        if not stock:
            return None

        item, created = WatchlistItem.objects.get_or_create(
            watchlist=watchlist,
            stock=stock,
        )
        return item

    def send_watchlist_alert(user, message):
        NotificationChannel.send_stock_alert({
            "user_id": user.id,
            "message": message,
        })

    @staticmethod
    def remove_stock(watchlist, symbol):
        stock = Stock.objects.filter(symbol=symbol).first()
        if not stock:
            return

        WatchlistItem.objects.filter(
            watchlist=watchlist,
            stock=stock
        ).delete()
