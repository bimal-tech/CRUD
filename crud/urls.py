from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_detail', views.add_details, name="add_details"),
]
