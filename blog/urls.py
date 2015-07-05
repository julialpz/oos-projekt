#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Julia Wallmüller'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/$', views.year, name='year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.month, name='month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w\-]+)/$', views.post, name='post'),
    url(r'^kategorie/(?P<slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^suche/$', views.search, name='search'),
    url(r'^kontakt/(?P<slug>[danke]+)/$', views.page, name="confirm"),
    url(r'^(?P<slug>[\w\-]+)/$', views.page, name='page'),
]

