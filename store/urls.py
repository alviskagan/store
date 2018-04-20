from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('detail_produk/<int:id_produk>', views.detail_produk, name="detail_produk"),
    
    # path('signup/', views.signup, name='signup'),
    # path('HomePelanggan/', views.home_pelanggan, name='home_pelanggan' ),
    #path('login/', auth_views.login, name='login'),
    # path('connection/', views.formView, name='loginform'),
    # path('login/', login, name='login'),
    #path('logout/', auth_views.logout, name='logout')
    # path('login/', login, {'template_name': 'store/registration/login.html'}),
]
