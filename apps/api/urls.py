from django.urls import path, include
from .views_auth import LoginView, RefreshView

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="jwt_login"),
    path("auth/refresh/", RefreshView.as_view(), name="jwt_refresh"),

    path("v1/", include([
        path("stocks/", include("apps.stocks.api.urls")),
        path("blog/", include("apps.blog.api.urls")),
        path("watchlists/", include("apps.watchlist.api.urls")),
    ])),
]
