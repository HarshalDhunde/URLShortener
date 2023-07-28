from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('',views.homepage),
    path('hello',views.helloWorld),
    path('task',views.task),
    path('all-analytics',views.analytics),
    path('<slug:customname>',views.redirect_url)
]