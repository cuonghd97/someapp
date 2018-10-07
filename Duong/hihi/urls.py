from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinfo),
    path('thank/',views.thankyou),
    path('codes/', views.codes),
    path('users/', views.showusers),
    path('data/', views.data)
]
