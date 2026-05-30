from .models import Watchlist


class WatchlistSelector:

    @staticmethod
    def get_user_watchlists(user):
        return Watchlist.objects.filter(user=user)
        return user.watchlists.prefetch_related("items__stock")

    @staticmethod
    def get_watchlist_items(watchlist):
        return watchlist.items.select_related("stock").all()
        return watchlist.items.select_related("stock")
