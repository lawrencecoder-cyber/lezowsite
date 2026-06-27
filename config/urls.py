from django.contrib import admin
from django.urls import include, path

from apps.common.views import health_check

urlpatterns = [

    # Home page
    path("", include("apps.common.urls")),

    # Admin
    path("admin/", admin.site.urls),

    # Authentication
    path("accounts/", include("apps.accounts.urls")),

    # Blog
    path("blog/", include("apps.blog.urls")),

    # Stocks
    path("stocks/", include("apps.stocks.urls")),

    # Dashboard
    path("dashboard/", include("apps.dashboard.urls")),

    # Watchlist
    path("watchlist/", include("apps.watchlist.urls")),

    # Notifications
    path(
        "notifications/",
        include("apps.notifications.urls")
    ),

    # Analytics
    path(
        "analytics/",
        include("apps.analytics.urls")
    ),

    # API
    path("api/", include("apps.api.urls")),

    # Health check
    path("health/", health_check, name="health"),
]
