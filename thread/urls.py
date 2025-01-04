from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.threads_list, name="threads_list"),
    path("<slug:slug>/", include("post.urls")),
    path("create/", views.create_thread, name="create_thread"),
    path("<slug:slug>/", views.thread_page, name="thread_page"),
    path("<slug:slug>/edit/", views.edit_thread, name="edit_thread"),
    path("<slug:slug>/delete/", views.delete_thread, name="delete_thread"),
]
