from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserCreationForm, UserCreateForm
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.


class SignUp(CreateView):
    form_class= UserCreateForm
    success_url= reverse_lazy('login')
    template_name= 'registration/sign_up.html'



    

    


# def register(request):
#       if request.method == 'POST':
#             form= UserCreationForm
#             if form.is_valid():
#                   user= form.save() 
#                   return redirect('')

