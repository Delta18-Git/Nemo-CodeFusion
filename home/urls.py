from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.helloworld,name='first'),#homepage
    path('home/',views.loginPage,name='home'),#login
    path('logout/',views.logoutPage,name='logout'),
    path('home/signup/',views.signuppage,name='signup'),
    path('idmake/',views.idmakepage,name='IDmake'),
    path('main/',views.mainpage,name='main'),
    path('income_input/',views.Income_input,name='income_input'),  
    path('outgo_input/',views.Outgo_input,name='outgo_input'),   
    path('view_balance/',views.View_balance,name='balance'),
    path('loan/',views.loan, name='loan'),
    path('subscriptions/',views.subscriptions,name='subscriptions'),
    path('accounts/',views.Accounts,name='accounts'),
    path('mails/',views.emails,name='emails'),
    path('groups/',views.Groups_page,name='groups'),

]