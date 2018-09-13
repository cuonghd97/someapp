from django.shortcuts import render
from .models import table
from django.http import HttpResponse
# Create your views here.

def index(request):
    data =  table.objects.all()
    for datas in data:
        print(datas.names)

    return render(request, 'pages/home.html',{'data':data})