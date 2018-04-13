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

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('', views.index, name = 'index'),
    path('', include("store.urls")),

    #path('login/', auth_views.login, name='login'),
    #path('logout/', auth_views.logout, name='logout')
    #url(r'^admin/', admin.site.urls),
    #path('store/shop/', include('store.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
#+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
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
       