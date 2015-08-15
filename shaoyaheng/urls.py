#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url

from shaoyaheng import views

urlpatterns = [
    url(r'^page/(?P<page_num>[\d]+)/$', views.page_view, name='page_view'),
    url(r'^page/exit/$', views.page_exit_view, name='page_exit_view'),
    url(r'^accounts/login/$', views.login_view, name='login_view'),
]
