# create api url endpoints 
from django.urls import path
from . import views_list

urlpatterns = [
    path('lists', views_list.getLists), # /lists
    path('list', views_list.getListItems), # /list?user_id={user_id}
    path('list/items', views_list.getAllItems), # /list/items?user_id={user_id}
    path('list/addItem', views_list.addItem), # /list/addItem?user_id={user_id}&list_id={list_id}&item_id={item_id}
    path('list/deleteItem', views_list.deleteItem), # /list/deleteItem?user_id={user_id}&list_id={list_id}&item_id={item_id}
    path('list/add', views_list.addList), # /list/add?user_id={user_id}&list_name={list_name}
    path('list/delete', views_list.deleteList), # /list/delete?user_id={user_id}&list_id={list_id}
]