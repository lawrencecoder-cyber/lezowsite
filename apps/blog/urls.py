from django.urls import path
from .views import blog_list_view, blog_detail_view, create_post_view

urlpatterns = [
    path("", blog_list_view, name="blog_list"),
    path("create/", create_post_view, name="create_post"),
    path("<slug:slug>/", blog_detail_view, name="blog_detail"),
]
