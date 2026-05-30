from apps.stocks.models import Stock


def market_context(request):
    return {
        "market_open": True,
        "top_movers": Stock.objects.order_by("-percent_change")[:5]
    }
