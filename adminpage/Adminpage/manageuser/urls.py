from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('informations/', views.informations),
    path('info/', views.info)
]
