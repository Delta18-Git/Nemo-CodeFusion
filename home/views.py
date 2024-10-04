import datetime
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from django.contrib import messages #this is what we import to get flash messages.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #imported for the user login
from django.contrib.auth.decorators import login_required,user_passes_test #this is used to restrict pages that need login or a certain login.
from django.utils import timezone
from .models import *
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def helloworld(request):
    return(render(request,'firsthack.html'))

