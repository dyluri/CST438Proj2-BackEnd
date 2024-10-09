# create api url endpoints 
from django.urls import path
from . import views_list
from . import views_user
from . import views_item
urlpatterns = [
    path('lists', views_list.getLists), # /lists  also has /lists?user_id={user_id}
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
    # not meant to be used on the front end
    path('debugitems', views_item.getItems), 

    path('items', views_item.allFunctionsItems) # has 4 different methods: 
    # GET: /items?list_id={list_id}  gets all items in a list
    # GET : /items?item_id={item_id} gives an item based off item_id
    # GET : /items?search={search}   searches for an item based on name
    # GET : /items?user_id={user_id} gets all items a user has in all their lists

    # The following will not work with the ?= format and have to be passed in as a form
    # POST : item_name list_id OPTIONAL: item_name item_url image_url price quantity description
    # returns: item that was made

    # DELETE: item_id

    # PATCH: item_id, OPTIONAL: item_name item_url image_url price quantity description
    # returns: item you patched
]