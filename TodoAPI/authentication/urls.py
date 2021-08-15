from django.contrib import admin
from django.urls import path, include
from .views import LoginView,RegisterUser

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterUser.as_view())

]
