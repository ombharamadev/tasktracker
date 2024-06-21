"""
URL configuration for tasktracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page,name="Main Page"),
    
    
    path('dashboard',views.dash,name="Dashboared Page"),
    path('update/<str:task_id>',views.updatedata,name="Update Page"),
    path('delete/<str:task_id>',views.deletedata,name="Delete Page"),
    
    
    
    path('api/hello',views.hello.as_view(),name='hello_world_api'),

    path('api/register',views.UserRegistrationView.as_view(),name='Register'),
    path('api/login',views.userlogin.as_view(),name="Login Process"),

    path('api/addtask',views.addtask.as_view(),name="Add Task"),
    path('api/assignto',views.addassignto.as_view(),name="assign Task"),
    
    path('api/getemaillist',views.getemaillist.as_view(),name="List of Email "),
    
    path('api/gettasklist',views.gettasklist.as_view(),name="List of Email "),
    
    path('api/getassignlist',views.getassignlist.as_view(),name="List of Email "),

    path('api/gettodolist',views.gettodolist.as_view(),name="List of Email "),
    path('api/getinproglist',views.getinprolist.as_view(),name="List of Email "),
    path('api/getdonelist',views.getdonelist.as_view(),name="List of Email "),


    path('api/deletepost',views.deletetask.as_view(),name="List of Email "),
    

]
