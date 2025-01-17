from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/api/exotic_flowers/', views.api_exotic_flowers, name="api_exotic_flowers"),
    path('/api/photo_salon/', views.api_photo_salon, name="api_photo_salon"),
    path('/api/production_center/', views.api_production_center, name="api_production_center"),
]
