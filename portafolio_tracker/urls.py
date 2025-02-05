from django.urls import path, include
from . import views
from django.shortcuts import render 

urlpatterns=[path('', views.SignUp.as_view(), name= 'createuser'),
             path('account/', include("django.contrib.auth.urls"), name= 'login'),
             ]