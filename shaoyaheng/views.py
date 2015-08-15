#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from shaoyaheng.models import UserProfile, UserProfileForm, Page

def login_view(request):
    if request.method == 'POST':
        login_form = UserProfileForm(request.POST)
        if login_form.is_valid():
            return HttpResponseRedirect(reverse('shaoyaheng:page_view', args=(1,)))
    else:
        login_form = UserProfileForm()
    return render(
        request,
        'shaoyaheng/login.html',
        {
            'login_form' : login_form,
        }
    )

def page_view(request, page_num):
    page = Page.objects.filter(page_num=int(page_num)).first()
    return render(
        request,
        'shaoyaheng/page.html',
        {
            'page' : page,
        }
    )

def page_exit_view(request):
    return HttpResponse(' ')
