"""online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    1. Add an import:  from other_app.views import Home
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#table of content dari website
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='store/registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/registration/logged_out.html'), name="logout"),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='store/registration/password_change_form.html'), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/registration/password_reset_form.html', email_template_name='store/registration/password_reset_email.html'), name="password_reset"),
    path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='store/registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='store/registration/password_reset_complete.html'), name="password_reset_complete"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='store/registration/password_reset_done.html'), name="password_reset_done"),
    
    #path('', views.index, name = 'index'),
    path('', include("store.urls")),
    path('signup/', views.signup, name='signup'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),             
    ]
    #[ path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})]
    #static(settings.STATIC_URL, doucment_root= settings.STATIC_ROOT),
 #        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
  #      'document_root': settings.MEDIA_ROOT}),
       