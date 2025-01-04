from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.forum_detail, name="forum_detail"),
]
