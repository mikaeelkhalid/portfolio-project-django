
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static
import jobs.views
from . import views
from django.shortcuts import render, get_object_or_404

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    
]