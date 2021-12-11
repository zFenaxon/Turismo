from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, "Core/index.html")

def login(request):
    return render(request,'Core/Login.html')

def Test (request):
    return render(request,'Core/Test.html')