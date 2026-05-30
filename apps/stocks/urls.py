from django.urls import path
from .views import stock_list_view, stock_detail_view

urlpatterns = [
    path("", stock_list_view, name="stocks"),
    path("<str:symbol>/", stock_detail_view, name="stock_detail"),
]
