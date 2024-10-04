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
from .forms import SignUpForm
from .models import *

def helloworld(request):
    return(render(request,'firsthack.html'))


def loginPage(request):
    if request.user.is_authenticated:
        return(redirect('main'))#TODO change this to main
    if request.method=="POST":
        username=request.POST.get('Fusn')#user.username
        password=request.POST.get('Fpwd')
        email=request.POST.get('email') #figure out how to take this during signup
        try: 
            
            user=User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist. Please sign up instead.')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return(redirect('main'))#TODO change to main
        else:
            messages.error(request,"Username and password don't match.")
    
    context={}
    return(render(request,'login.html',context))

@login_required(login_url='home') #just in case.
def logoutPage(request):#removed GI stuff
    logout(request) 
    return(redirect('home'))


def signuppage(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after signup
                messages.success(request, 'Signup successful!')
                return redirect('IDmake')  # Redirect to a home page or another view
        else:
            form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    except:
        return(redirect('IDmake'))

@login_required(login_url='home')
def idmakepage(request): #Users have a unique USer ID
    try:
        IDCard.objects.get(user=request.user)
    except: #if user doesnt have an id after sign up
        if request.method=="POST":
            myID=request.POST.get('Fuid')
            mybal=request.POST.get('Fbal')
            try: 
                test=IDCard.objects.get(UserID=myID)
                messages.error(request,'User ID taken, try again.')
            except:
                ID=IDCard.objects.create(user=request.user,UserID=myID)
                bala=Balance.objects.create(user=request.user,amount=bal)#automated balance creation
                return(redirect('home'))
        else:
            return(render(request,'cardpage.html'))
    return(redirect('main'))#TODO change to main

@login_required(login_url='home')
def mainpage(request):
    return(render(request,'mainpage.html'))

@login_required(login_url='home')
def Income_input(request):
    user = request.user
    if request.method == "POST":
        amount = Decimal(request.POST.get('Famount'))
        dtime = request.POST.get('FDtime')
        source = request.POST.get('Fsource')
        comments = request.POST.get('Fcomments')
        bal=Balance.objects.get(user=user)
        bal.amount=bal.amount + amount
        bal.save()
        inc = Income.objects.create(user=user, Amount=amount, DTime=dtime, Source=source, comments=comments)
        
    return render(request, 'income.html')

@login_required(login_url='home')
def Outgo_input(request): #TODO REciept upload
    user = request.user
    if request.method == "POST":
        amount = request.POST.get('Famount')
        dtime = request.POST.get('FDtime')
        where = request.POST.get('Fwhere')
        why = request.POST.get('Fwhy')
        comments = request.POST.get('Fcomments')
        bal=Balance.objects.get(user=user)
        bal.amount-=amount
        Balance.save()
        out = Outgo.objects.create(user=user, Amount=amount, DTime=dtime, Where=where ,Why=why ,comments=comments)
    return(render(request,'outgo.html'))

@login_required(login_url='home')
def View_balance(request):
    bal=Balance.objects.get(user=request.user).amount
    print(bal)
    context={'bal':bal}
    return(render(request,'viewbalance.html',context))

@login_required(login_url='home')
def loan(request):
    user=request.user
    if request.method=="POST":
        loan_amount = request.POST.get('FLamount')
        annual_interest_rate= request.POST.get('Finterest')
        loan_tenure = request.POST.get('Ftenure')
        loan=Loan.objects.create(user=user,loan_amount=loan_amount,loan_tenure=loan_tenure,annual_interest_rate=annual_interest_rate)
    return(render(request,'loan.html'))


@login_required(login_url='home')
def subscriptions(request):
    if request.method=="POST":
        sub_amount = request.POST.get('FSamount')
        sub_tenure= request.POST.get('Ftenure')
        sub=Subscriptions.objects.create(user=request.user,sub_amount=sub_amount,sub_tenure=sub_tenure)
    return(render(request,'subscriptions.html'))


# TAXES, (Accounts?), Groups/clubs (head oversees expenses, approves?) User can create club/group and be the admin of it and change who the admins are. )
