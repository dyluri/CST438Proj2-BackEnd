# create api url endpoints 
from django.urls import path
from . import views_list
from . import views_user
from . import views_item
urlpatterns = [
    path('lists', views_list.getLists), # /lists
    path('lists/list', views_list.getListItems), # /lists/list?list_id={list_id}
    path('lists/items', views_list.getAllItems), # /lists/items?user_id={user_id}
    path('lists/addItem', views_list.addItem), # /lists/addItem?user_id={user_id}&list_id={list_id}&item_id={item_id}
    path('lists/deleteItem', views_list.deleteItem), # /lists/deleteItem?user_id={user_id}&list_id={list_id}&item_id={item_id}
    path('lists/add', views_list.addList), # /lists/add?user_id={user_id}&list_name={list_name}
    path('lists/delete', views_list.deleteList), # /lists/delete?user_id={user_id}&list_id={list_id}
    path('login/admin', views_user.adminLogIn), #/login/admin?username={username}&password={password}
    path('users/delete', views_user.adminDeleteUser), #/users?username={username}&user_id={user_id}
    path('users/update', views_user.updateUser), #/users?username={username}&user_id={user_is}&new_username={new_username}&new_password={new_password}
    path('', views_user.homePage),
    path('users', views_user.getAllUsers),
    path('newuser', views_user.createUser),
    path('login', views_user.logIn),
    path('logout', views_user.logout_or_delete_account),
    path('debug', views_item.getItems)
]