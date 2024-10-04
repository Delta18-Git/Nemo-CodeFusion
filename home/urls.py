from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.helloworld,name='first'),#homepage
    path('home/',views.loginPage,name='home'),#login
    path('logout/',views.logoutPage,name='logout'),
    path('home/signup/',views.signuppage,name='signup'),
    path('idmake/',views.idmakepage,name='IDmake'),
]