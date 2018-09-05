from django.shortcuts import render
from django.http import HttpResponse
from .models import USER
# Create your views here.

def list(request):
    Data = {"users": USER.objects.all()}
    return render(request, 'blogs/blog.html', Data)
def detail(request, id):
    detail = USER.objects.get(id = id)
    return render(request, 'blogs/detail.html', {"user": detail})
