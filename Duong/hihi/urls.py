from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinfo),
    path('thank/',views.thankyou)
]
