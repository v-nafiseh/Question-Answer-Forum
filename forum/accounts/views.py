from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    return render(request, 'accounts/login.html')