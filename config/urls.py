from django.contrib import admin
from django.urls import path, include
from apps.common.views import health_check

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("apps.accounts.urls")),
    path("stocks/", include("apps.stocks.urls")),
    path("blog/", include("apps.blog.urls")),
    path("health/", health_check),
    path("api/", include("apps.api.urls")),
]
