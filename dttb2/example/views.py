from django.shortcuts import render
from .models import table
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    response  = HttpResponse()
    data = []
    table_data = table.objects.all()
    for dt in table_data:
        data.append([dt.id, dt.names, dt.age])
    datas = {"data": data}
    json_datas = json.loads(json.dumps(datas))
    # json = serializers.serialize('json', table_data)
    datajs = json.dumps(datas)
    return JsonResponse(json_datas)

def dttable(request):
    response = HttpResponse()
    if request.method == 'POST':
        a = table.objects.get(id = request.POST['id'])
        a.names = request.POST['names']
        a.age = request.POST['age']
        a.save()
    return render(request, 'pages/home.html')

# def getTable(request):
#     a = table.objects.all();
