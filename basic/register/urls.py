from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('', views.index, name='home'),
]