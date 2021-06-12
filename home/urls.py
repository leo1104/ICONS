
from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    
    path("",views.index,name='home'),
    path("test",views.test,name='test'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("faculty",views.faculty,name='faculty'),
    path("login",views.login,name='login'),
    path("news",views.news,name='news'),
    path("schedule",views.schedule,name='schedule'),
    path("register",views.register,name='register'),
    path("contactus",views.contactus,name='home'),
    path("alumni",views.alumni,name='alumni'),
    path("base",views.base,name='base'),
    path("logout",views.logout,name='logout'),



]
