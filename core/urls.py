# coding: utf-8
from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
