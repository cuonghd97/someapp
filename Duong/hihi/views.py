from django.shortcuts import render
from . import models
from .forms import userInfo
from django.http import HttpResponse, HttpResponseRedirect
from random import randint



# Create your views here.

def userinfo(request):
    if request.method == 'POST':
        models.userInfo.objects.create(userName = request.POST['userName'], email = request.POST['email'], birthday = request.POST['birthday'])
    #     response = HttpResponse()
        return HttpResponseRedirect('/thank')
    # userinfo = userInfo()
    return render(request, 'pages/index.html')

def thankyou(request):
    response = HttpResponse()
    # Data = {'codes': models.Code.objects.all()}
    records = models.Code.objects.count()
    randomrc = randint(1, int(records))
    # response.write(randomrc)
    # return responses
    randomdata = models.Code.objects.get(id = int(randomrc))
    Data = {'code': randomdata}
    return render(request,"pages/thankyou.html", Data)