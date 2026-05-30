from django.shortcuts import render, redirect
from .models import Notification, PriceAlert
from apps.stocks.models import Stock


def notifications_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    notifications = Notification.objects.filter(user=request.user)
    alerts = PriceAlert.objects.filter(user=request.user)

    return render(request, "notifications/list.html", {
        "notifications": notifications,
        "alerts": alerts
    })


def create_alert_view(request):
    if request.method == "POST":
        symbol = request.POST.get("symbol")
        price = request.POST.get("price")

        stock = Stock.objects.filter(symbol=symbol).first()

        if stock:
            PriceAlert.objects.create(
                user=request.user,
                stock=stock,
                target_price=price
            )

    return redirect("notifications")
