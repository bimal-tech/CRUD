from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import operationSerializer

# REST Frameworks

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/all_detail',
        'detail view': '/details/<str:pk>',
        'create': '/add-details/',
        'update': '/edit/<str:pk>/',
        'delete': '/delete/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def all_detail(request):
    datas = operation.objects.all()
    serializer = operationSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_details(request):
    serializer = operationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def edit(request, pk):
    datas = operation.objects.get(id=pk)
    serializer = operationSerializer(instance=datas, data=request.data)

    if serializer.is_valid():
        serializer.save()


@api_view(['DELETE'])
def delete(request, pk):
    datas = operation.objects.get(id=pk)
    datas.delete()
    msg = "The item " + str(pk) + " is deleted"
    return Response(msg)


@api_view(['GET'])
def details(request, pk):
    datas = operation.objects.get(id=pk)
    serializer = operationSerializer(datas, many=False)
    return Response(serializer.data)
