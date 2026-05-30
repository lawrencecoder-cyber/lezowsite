from django.shortcuts import render
from .models import Stock


def stock_table_view(request):

    stocks = Stock.objects.all()

    if request.headers.get("HX-Request"):
        return render(request, "components/stock_table.html", {
            "stocks": stocks
        })

    return render(request, "stocks/page.html", {
        "stocks": stocks
    })
