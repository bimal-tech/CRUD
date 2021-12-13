from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_detail', views.add_details, name="add_details"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),

]
