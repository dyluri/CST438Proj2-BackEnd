# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from base.models import Lists
from .serializers import ListsSerializer

#Gets all the Lists
@api_view(['GET'])
def getLists(request):
    lists = Lists.objects.all()
    serializer = ListsSerializer(lists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Gets list of items in a specific list (DOESN'T GET ITEMS' INFO JUST THE ID LIST)
#This function will be used for the item functions
@api_view(['GET'])
def getListItems(request):
    list_id = request.GET.get('list_id')
    
    try:
        list_instance = Lists.objects.get(list_id=list_id)
    except Lists.DoesNotExist:
        return Response({'error':'List not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListsSerializer(list_instance)
    return Response(serializer.data, status=status.HTTP_200_OK) 

#Gets all items in all of the user's lists (DOESN'T GET ITEMS' INFO JUST THE ID LIST)
#This function will be used for the item functions
@api_view(['GET'])
def getAllItems(request):
    user_id = request.GET.get('user_id')
    item_list_instances = Lists.objects.filter(user_id=user_id).filter(~Q(item_list__isnull=True) & ~Q(item_list__exact='')).values_list('item_list', flat=True)
    all_items = []

    if not item_list_instances:
        return Response({'error':'No item lists found for this user'}, status=status.HTTP_404_NOT_FOUND)
    
    for item_list in item_list_instances:
        all_items.extend(item_list.split(','))

    return Response(all_items, status=status.HTTP_200_OK)

#Add the item_list (THIS ONLY ADDS THE ITEM ID TO THE item_list in the list table)
@api_view(['POST'])
def addItem(request):
    user_id = request.GET.get('user_id')
    list_id = request.GET.get('list_id')
    item_id = request.GET.get('item_id')

    try:
        list_instance = Lists.objects.get(list_id=list_id, user_id=user_id)
    except Lists.DoesNotExist:
        return Response({'error':'List not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    existing_items = list_instance.item_list.split(',')
    
    if item_id not in existing_items:
        existing_items.append(item_id)
    
    list_instance.item_list = ','.join(existing_items)
    list_instance.save()

    serializer = ListsSerializer(list_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Deletes the item_list (THIS ONLY DELETES THE ITEM ID TO THE item_list in the list table)
@api_view(['POST'])
def deleteItem(request):
    user_id = request.GET.get('user_id')
    list_id = request.GET.get('list_id')
    item_id = request.GET.get('item_id')

    try:
        list_instance = Lists.objects.get(list_id=list_id, user_id=user_id)
    except Lists.DoesNotExist:
        return Response({'error':'List not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    existing_items = list_instance.item_list.split(',')
    
    if item_id in existing_items:
        existing_items.remove(item_id)
    
    list_instance.item_list = ','.join(existing_items)
    list_instance.save()

    serializer = ListsSerializer(list_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Creates a new list
@api_view(['Post'])
def addList(request):
    list_name = request.GET.get('list_name')
    user_id = request.GET.get('user_id')

    if Lists.objects.filter(list_name=list_name,user_id=user_id).exists():
        return Response({'error': 'List with this name already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

    listObject = Lists.objects.create(list_name=list_name, user_id=user_id)
    serializer = ListsSerializer(listObject)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# Deletes the list with the same list_id
@api_view(['DELETE'])
def deleteList(request):
    user_id = request.GET.get('user_id')
    list_id = request.GET.get('list_id')

    try:
        list_instance = Lists.objects.get(list_id=list_id, user_id=user_id)
        list_instance.delete()
        return Response(status=status.HTTP_200_OK)
    except Lists.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

