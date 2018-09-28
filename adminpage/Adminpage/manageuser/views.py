from django.shortcuts import render
from . import models
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def informations(request):
    return render(request, 'pages/informations.html')
def info(request):
    data = []
    table_data = models.UserInfo.objects.all()
    for dt in table_data:
        data.append([dt.id, dt.username, dt.password, dt.fullname, dt.address, dt.phone, dt.email, dt.typeuser])
    datas = {"data": data}
    json_datas = json.loads(json.dumps(datas))
    return JsonResponse(json_datas)