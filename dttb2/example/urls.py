from django.urls import path
from . import views

urlpatterns = [
    path('', views.dttable),
    path('index', views.index)
]
