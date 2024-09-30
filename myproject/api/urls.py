from django.urls import path
from . import views_user

urlpatterns = [
    path('', views_user.homePage),
    path('users', views_user.getAllUsers),
    path('newuser', views_user.createUser),
    path('login', views_user.logIn),
    path('logout', views_user.logout_or_delete_account),
]