"""
URL configuration for myproject project.

The 'urlpatterns' list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from first_app import views

# from second_app import views as v2

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("",include("first_app.urls")),
    path("second/",include("second_app.urls")),
]


# path("",views.demo),
# path("home/",views.home),
# path("about/",views.about),
# path("contact/<x>/",views.contact),     #x is the route parameter
# path("page/<y>/",views.page),
# path("login/<pwd>",views.login),
# path("homepage/",views.homepage),
# path("aboutpage/",views.aboutpage),
# path("contactpage/",views.contactpage, name = "cn"),

# path("home2/",v2.home)


# from this my code   -->  from first_app import views
# path("",views.demo)  -->  "" -- means first page, in this views.demo --> calls the file views inside the file demo function 
# path("home/",views.demo)   -->  "home/" -- url route extension



