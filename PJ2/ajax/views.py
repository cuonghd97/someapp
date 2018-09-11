from django.shortcuts import render
from .models import user
from django.http import HttpResponse
# Create your views here.

def ajax(request):
    if request.method == 'POST':
        user.objects.create(username = request.POST['username'], password = request.POST['password'])
    return render(request, 'pages/home.html')