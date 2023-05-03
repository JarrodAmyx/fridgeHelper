from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("loginpage/", views.gotologin, name="loginpage"),
    path("registerpage/", views.gotoregister, name="registerpage"),
    path("register/",views.register,name="register"),
    path("varifyLogin/", views.varifylogin, name="varifyLogin"),
    path("homepage/", views.gotohomepage, name = "homepage"),
    path("addfridgtoDB/", views.addFridgetoDB, name="addfridgepage"),
    path("fridgepage/", views.gotoFridge, name="fridgepage"),
    path("accessFridge/", views.accessFridge, name="accessFridge"),
    path("add_removeitemform/", views.add_removeitemform, name="add_removeitemform"),
    path("additemtofridge/", views.additemtofridge, name="additemtofridge"),
    path("additemtofreezer/", views.additemtofreezer, name="additemtofreezer"),
    path("additem/", views.additem, name="additem"),
    path("gotofridgeshelf/", views.gotofridgeshelf, name="gotofridgeshelf"),
    path("gotofreezershelf/", views.gotofreezershelf, name="gotofreezershelf"),
    path("removeitemfromfridge/", views.removeitemfromfridge, name="removeitemfromfridge"),
    path("removeitemfromfreezer/", views.removeitemfromfreezer, name="removeitemfromfreezer"),
    path("removeitem/", views.removeitem, name="removeitem"),
    path("add_removeUser/", views.add_removeUser, name="add_removeUser"),
    path("varify_add_User/", views.varify_add_User, name="varify_add_User"),
    path("varify_remove_user/", views.varify_remove_user, name="varify_remove_user"),
    path("createFridge/", views.createFridge, name="createFridge"),
]