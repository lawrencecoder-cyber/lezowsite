from django.shortcuts import render, redirect, get_object_or_404
from .selectors import WatchlistSelector
from .services import WatchlistService
from .models import Watchlist


def watchlist_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    watchlists = WatchlistSelector.get_user_watchlists(request.user)

    return render(request, "watchlist/list.html", {
        "watchlists": watchlists
    })


def create_watchlist_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        WatchlistService.create_watchlist(request.user, name)

    return redirect("watchlist")


def add_stock_view(request, watchlist_id):
    watchlist = get_object_or_404(Watchlist, id=watchlist_id)

    symbol = request.POST.get("symbol")
    WatchlistService.add_stock(watchlist, symbol)

    return redirect("watchlist")


def remove_stock_view(request, watchlist_id, symbol):
    watchlist = get_object_or_404(Watchlist, id=watchlist_id)

    WatchlistService.remove_stock(watchlist, symbol)

    return redirect("watchlist")
