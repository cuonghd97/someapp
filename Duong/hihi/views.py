from django.shortcuts import render
from . import models
from .forms import userInfo
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from random import randint
import json


# Create your views here.

def userinfo(request):
    if request.method == 'POST':
        models.userInfo.objects.create(userName = request.POST['userName'], email = request.POST['email'], birthday = request.POST['birthday'])
        return HttpResponseRedirect('/thank')
    return render(request, 'pages/index.html')

def thankyou(request):
    response = HttpResponse()
    list = []
    nonactive = models.Code.objects.exclude(active = '1')
    for item in nonactive:
        list.append(item)
    count = len(list)
    random = randint(1, count)
    response.write(list[random])
    data = models.Code.objects.get(code = list[random])
    data.active = '1'
    data.save()
    Data = {'code': data}
    return render(request,"pages/thankyou.html", Data)

def codes(request):
    if request.method == 'POST':
        models.Code.objects.create(code = request.POST['code'], active = '0')
    tbl_code = models.Code.objects.all()
    data = {'codes': tbl_code}
    return render(request, "pages/codes.html", data)

def data(request):
    data = []
    table_data = models.Code.objects.all()
    for dt in table_data:
        data.append([dt.code, dt.active])
    datas = {"data": data}
    json_datas = json.loads(json.dumps(datas))
    # json = serializers.serialize('json', table_data)
    datajs = json.dumps(datas)
    return JsonResponse(json_datas)

def showusers(request):
    response = HttpResponse()
    tbl_users = models.userInfo.objects.all()
    data = {'users': tbl_users}
    return render(request, 'pages/users.html', data)