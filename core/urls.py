# coding: utf-8
from django.conf.urls import patterns, url
from core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
