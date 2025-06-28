from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"home2.html")

def main(request):
    return render(request,"app2/main.html")
