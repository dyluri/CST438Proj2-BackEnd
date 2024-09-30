# create api url endpoints 
from django.urls import path
from . import views

urlpatterns = [
    path('lists', views.getLists),
    path('lists/add', views.addList),
    path('lists/delete/<int:pk>/', views.deleteList)

]