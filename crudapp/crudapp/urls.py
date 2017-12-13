"""crudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url, include
from django.contrib import admin
from crudapp.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog_posts/', include('blog_posts.urls', namespace='blog_posts')),
    url(r'^$', home, name='home' ),
]
