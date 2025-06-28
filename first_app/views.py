from django.shortcuts import render,HttpResponse

# Create your views here.

def demo(request):          #the request which has been send by the user 
    return HttpResponse("Hello World")     #response will be as the request is given

def home(request):
    return HttpResponse("Welcome to Home page")

def about(request):
    a = 10
    return HttpResponse(f"About page {a}")

def contact(request,x):
    return HttpResponse(f"Contact page {x}")

def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")

def page(request,y):
    x = "Harini"
    z = range(10)
    return render(request,"neww.html",{"a":x, "b":y, "c":z})

def login(request,pwd):
    password = "Harini1234"
    return render(request,"authen.html",{"p" : pwd,"q" : password})
