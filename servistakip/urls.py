"""servistakip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    #url(r'^anlasmalar/$', anlasmalar, name='anlasmalar'),
    #url(r'^servisler/$', servisler, name='servisler'),
    #url(r'^musteriler/$', musteriler, name='musteriler'),
    #url(r'^musteri_detay/(?P<musteri_id>[0-9]+)/$', musteri_detay, name='mus_detay'),
    #url(r'^cihazservisler/$', cihazservisler, name='cihazservisler'),
    #url(r'^hosting/$', hostingler, name='hostingler'),
]

urlpatterns += staticfiles_urlpatterns()