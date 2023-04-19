from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("loginpage/", views.gotologin, name="loginpage"),
    path("registerpage/", views.gotoregister, name="registerpage"),
    path("register/",views.register,name="register"),
    path("home/", views.login, name="home")
]