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
    pass



@api_view(['GET'])
def add_details(request):
    pass


@api_view(['GET'])
def edit(request):
    pass


@api_view(['GET'])
def delete(request):
    pass


@api_view(['GET'])
def details(request):
    pass
