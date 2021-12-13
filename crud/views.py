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
        item.rn = request.POST.get('rn')
        item.username = request.POST.get('username')
        item.age = request.POST.get('age')
        # print(item.sn)
        # print(item.username)
        # print(item.age)
        # item.sn = str(len(operation.objects.all())+1)
        item.save()
        return redirect('/')

    return render(request, "crud_templates/add_detail.html")


def edit(request, pk):
    print("pressed edit")
    datas = operation.objects.get(pk=pk)
    operation.objects.get(pk=pk).delete()
    return render(request, "crud_templates/edit.html", {
        "datas": datas
    })
    # return render(request, "crud_templates/index.html")


def delete(request, pk):
    print("pressed delete")
    operation.objects.get(pk=pk).delete()
    datas = operation.objects.all()
    return render(request, "crud_templates/index.html", {
        "datas": datas
    })
