from django.shortcuts import render, get_object_or_404
from .models import Stock


def stock_list_view(request):
    stocks = Stock.objects.all()

    if request.headers.get("HX-Request"):
        return render(
            request,
            "components/stock_table.html",
            {"stocks": stocks}
        )

    return render(
        request,
        "stocks/page.html",
        {"stocks": stocks}
    )


def stock_detail_view(request, symbol):
    stock = get_object_or_404(
        Stock,
        symbol=symbol
    )

    return render(
        request,
        "stocks/detail.html",
        {
            "stock": stock
        }
    )
