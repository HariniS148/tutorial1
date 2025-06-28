# from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls), 
    path("",home),
    path("home/",home),
    path("about/",about),
    path("contact/<x>/",contact),     #x is the route parameter
    path("page/<y>/",page),
    path("login/<pwd>",login),
    path("homepage/",homepage),
    path("aboutpage/",aboutpage),
    path("contactpage/",contactpage, name = "cn"),

    ]