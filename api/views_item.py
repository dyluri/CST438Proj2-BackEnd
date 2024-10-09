# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from base.models import Item, Lists
from .serializers import ItemSerializer

#Gets all the Lists
@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def allFunctionsItems(request):
    # GET: List or show a specific item
    if request.method == 'GET':
        item_id = request.GET.get('item_id')
        search = request.GET.get('search')
        user_id = request.GET.get('user_id')
        if item_id:
            item = get_object_or_404(Item, pk=item_id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)

        if search:
            items = Item.objects.filter(item_name__icontains=search)
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)
        if user_id:
            user_lists = Lists.objects.filter(user_id=user_id)
            items = Item.objects.filter(list__in=user_lists)
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)

        list_id = request.GET.get('list_id')
        if list_id:
            items = Item.objects.filter(list=list_id)
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)

        return Response({"error": "Request was missing item_id/search, or was missing list_id/item_name"})

    # POST: Add a new item
    elif request.method == 'POST':
        item_name = request.data.get('item_name')
        list_id = request.data.get('list_id')
        
        if not item_name and not list_id:
            return Response({"error": "item_name and list_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            list_object = Lists.objects.get(pk=list_id)
        except Lists.DoesNotExist:
            return Response({"error": "List does not exist"}, status=status.HTTP_404_NOT_FOUND)

        item = Item.objects.create(
            item_name=item_name,
            list = list_object,
            item_url=request.data.get('item_url', None),
            image_url=request.data.get('image_url', None),
            price=request.data.get('price', None),
            quantity=request.data.get('quantity', None),
            description=request.data.get('description', None)
        )

        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # DELETE: Remove an item by ID
    elif request.method == 'DELETE':
        # This structure means that passing parameters in the url works for easy debugging.
        item_id = request.GET.get('item_id')
        item_id = request.data.get('item_id', item_id)

        if not item_id:
            return Response({"error": "Item ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return Response({"message": f"Item {item_id} deleted"}, status=status.HTTP_200_OK)

    # PATCH: Update an item by ID
    elif request.method == 'PATCH':
        item_id = request.data.get('item_id')

        if not item_id:
            return Response({"error": "Item ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)

        item = get_object_or_404(Item, pk=item_id)

        item.item_name = request.data.get('item_name', item.item_name)
        item.item_url = request.data.get('item_url', item.item_url)
        item.image_url = request.data.get('image_url', item.image_url)
        item.price = request.data.get('price', item.price)
        item.quantity = request.data.get('quantity', item.quantity)
        item.description = request.data.get('description', item.description)

        item.save()

        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)