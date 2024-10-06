from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer
@api_view(['GET'])
def homePage(request):
    welcome = {'hi': 'welcome to the django api thingy. To see the response for any of these in json, put into the link the following \'format=json\' ',
              'links':['/newuser?username={username}&password={password}', 
                       '/login?username={username}&password={password}',
                       '/logout?username={username}',
                       '/logout?username={username}&password={password}',
                       '/users',
                        '/lists',
                        '/lists/list?list_id={list_id}',
                        '/lists/items?user_id={user_id}',
                        '/lists/addItem?user_id={user_id}&list_id={list_id}&item_id={item_id}',
                        '/lists/deleteItem?user_id={user_id}&list_id={list_id}&item_id={item_id}',
                        '/lists/add?user_id={user_id}&list_name={list_name}',
                        '/lists/delete?user_id={user_id}&list_id={list_id}',
                       ]}
    return Response(welcome)

# TODO: Make this admin only
@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many='true')
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    # Check if a user with the same username already exists
    username = request.data.get('username')
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def logIn(request):
    # Get the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Check if the user with the given username exists
    try:
        user = User.objects.get(username=username)
        if (password == user.password):
            # Update the signed_in field to True
            user.signed_in = True
            user.save()
            # Serialize and return the user data
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        else:
            return Response({"error": "Invalid password"}, status=400)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['PUT', 'DELETE'])
def logout_or_delete_account(request):
    username = request.data.get('username')
    print(username)
    try:
        # Get the user by username
        user = User.objects.get(username=username)
        
        if request.method == 'PUT':
            # Logout user (signed_in = False)
            if user.signed_in:
                user.signed_in = False
                user.save()
                return Response({"message": f"{username} has successfully logged out.", "result" : True}, status=200)
            else:
                return Response({"error": f"{username} is not signed in.", "result" : False}, status=400)
        
        elif request.method == 'DELETE':
            # For DELETE, confirm password before deleting the account
            password = request.data.get('password')
            
            if (password == user.password):
                user.delete()
                return Response({"message": f"Account for {username} has been deleted." , "result" : True}, status=200)
            else:
                return Response({"error": "Password incorrect.", "result" : False}, status=400)
    
    except User.DoesNotExist:
        return Response({"error": "User not found", "result" : False}, status=404)