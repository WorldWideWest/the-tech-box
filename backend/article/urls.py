from django.urls import path

from .views import get_all, get_by_id, get_by_title

urlpatterns = [
    path("articles/", get_all, name = "get_articles"),
    path("articles/<int:id>/", get_by_id, name = "get_article_by_id"),
    path("articles/<str:title>/", get_by_title, name = "get_article_by_title"),
]