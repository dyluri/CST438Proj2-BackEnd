from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer
@api_view(['GET'])
def homePage(request):
    welcome = {'hi': 'welcome to the django api thingy. To see the response for any of these in json, put into the link the following \'format=json\' ',
              'links':['/newuser?username={username}&password={password}', '/users']}
    return Response(welcome)

# TODO: Make this admin only
@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many='true')
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)