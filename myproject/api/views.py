# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Lists
from .serializers import ListsSerializer

# Create your views here.
@api_view(['GET'])
def getLists(request):
    lists = Lists.objects.all()
    serializer = ListsSerializer(lists, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def addList(request):
    serializer = ListsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteList(request, pk):
    try:
        list_instance = Lists.objects.get(pk=pk)
        list_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Lists.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)