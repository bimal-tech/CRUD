from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    datas = operation.objects.all()
    return render(request, "crud_templates/index.html", {
        "datas": datas
    })


def add_details(request):
    if request.method == "POST":
        item = operation()
        item.username = request.POST.get('username')
        item.age = request.POST.get('age')
        # print(item.sn)
        # print(item.username)
        # print(item.age)
        item.sn = str(len(operation.objects.all())+1)
        item.save()
        return redirect('/')

    return render(request, "crud_templates/add_detail.html")
