from django.contrib import admin
from django.urls import path , include
from intern4 import views

app_name = 'intern4'

urlpatterns =[
    path('',views.base,name='base'),
    path('newpage/',views.newpage,name='newpage'),
    path('getstarted/',views.getstarted,name='getstarted'),
]