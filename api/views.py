from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from targetManagement.models import Item, Category
from .Serializers import ItemSerializer, CategorySerializer

# Create your views here.
@api_view(['GET'])
def productsByCatID(request,catID):
    myCat = Category.objects.get(id=catID)
    items = Item.objects.filter(category=myCat)
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productsByID(request,id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        item = None
    serializer = ItemSerializer(item)
    return Response(serializer.data)


@api_view(['GET'])
def allCategories(request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats,many=True)
    return Response(serializer.data)
