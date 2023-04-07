from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('user_requests/', views.request_view, name='user_requests'),
]