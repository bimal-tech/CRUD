from django.urls import path
from . import views

urlpatterns = [
    path('crud/all_detail/', views.all_detail, name="index"),
    path('crud/details/<int:pk>', views.details, name="details"),
    path('crud/add_detail', views.add_details, name="add_details"),
    path('crud/edit/<int:pk>', views.edit, name="edit"),
    path('crud/delete/<int:pk>', views.delete, name="delete"),
    path('crud/', views.apiOverview, name="infos"),
]
