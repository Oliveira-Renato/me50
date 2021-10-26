from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("w", views.searchPage, name="searchPage"),
    path("wiki/page/new", views.create, name="create"),
    path("wiki/page/edit", views.edit, name="edit")
]
