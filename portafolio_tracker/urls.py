from django.urls import path, include
from . import views
from django.shortcuts import render 

urlpatterns=[path('/SignUp', views.SignUp.as_view(), name= 'createuser'),
             path('/Login', views.Login, name= 'login'),
             
             ]