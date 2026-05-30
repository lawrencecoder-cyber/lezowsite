from django.shortcuts import render
from .selectors import AnalyticsSelector


def analytics_dashboard(request):
    if not request.user.is_authenticated:
        return render(request, "errors/403.html")

    activity = AnalyticsSelector.user_activity(request.user)
    summaries = AnalyticsSelector.market_summaries()

    return render(request, "analytics/dashboard.html", {
        "activity": activity,
        "summaries": summaries,
    })
