from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('users', views.getAllUsers),
    path('newuser', views.createUser)
]