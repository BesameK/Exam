from django.contrib import admin
from django.urls import path

from ecommerce import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tickets/", views.tickets, name="tickets"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("createOrder/", views.createOrder, name="createOrder"),

]
