from django.urls import path
from .views import notifications_view, create_alert_view

urlpatterns = [
    path("", notifications_view, name="notifications"),
    path("create/", create_alert_view, name="create_alert"),
]
