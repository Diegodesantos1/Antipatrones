from django.contrib import admin
from django.urls import path
from CalculadoraWebApp import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.index, name="index"),
    path('guardar_operacion/', views.guardar_operacion, name='guardar_operacion'),
]