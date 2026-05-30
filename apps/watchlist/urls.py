from django.urls import path
from . import views

urlpatterns = [
    path("", views.watchlist_view, name="watchlist"),
    path("create/", views.create_watchlist_view, name="create_watchlist"),
    path("<int:watchlist_id>/add/", views.add_stock_view, name="add_stock"),
    path("<int:watchlist_id>/remove/<str:symbol>/", views.remove_stock_view, name="remove_stock"),
]
