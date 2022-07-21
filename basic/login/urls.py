from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [ 
    path('',views.loginUser, name="login"),
    path('',views.logoutUser,name="logout"),
]
