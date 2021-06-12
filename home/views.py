from django.shortcuts import render,HttpResponse,redirect
from home.models import ContactUs
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import News
 
# Create your views here.

# def index(request):
#     return(HttpResponse("this is home page"))

def index(request):
    return(render(request,"index.html"))

def dashboard(request):
    return(render(request,"dashboard.html"))
def faculty(request):
    return(render(request,"faculty.html"))

# def login(request):
#     return(render(request,"login.html"))

def news(request):
    # return(render(request,"news.html"))
    news_list=News.objects.all()
    return render(request,"news.html",{"news_list":news_list}) 

    
def schedule(request):
    return(render(request,"schedule.html"))
def alumni(request):
    return(render(request,"alumni.html"))

# def register(request):
#     if request.method == 'POST':
#         pass
        
#     return(render(request,"login.html"))
#!start
def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,"login.html")

def register(request):
    if(request.method=="POST"):
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        first_name=request.POST.get("first_name")

        if(1):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("login")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect("login")
            else:
                #this gets the data
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
                #this saves the data
                user.save()
                messages.info(request,"User Created")
                return redirect("login")
                
        else:
            messages.info(request,"Password not Matching")
            return redirect("login")
        return redirect("/")
    else:
        return render(request,"login.html")
#!end
def contactus(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        message=request.POST.get('message')
        contactus=ContactUs(email=email,message=message)
        contactus.save()
        # messages.success(request, 'Form Submitted :)') 


    return(render(request,"index.html"))

def base(request):
    return(render(request,"base.html"))
def test(request):
    return(render(request,"test.html"))

