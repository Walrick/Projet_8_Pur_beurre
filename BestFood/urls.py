#!/usr/bin/python3
# -*- coding: utf8 -*-

from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.index), # "/store" will call the method "index" in "views.py"
]