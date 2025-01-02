from django.urls import path
from . import views

urlpatterns = [
    path("", views.thread_list, name="thread_lists"),
    path("create/", views.create_thread, name="create_thread"),
]
