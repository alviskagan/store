from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    #path('produk/', views.produk, name='produk' ),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout')
]
