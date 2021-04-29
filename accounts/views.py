#!/usr/bin/python3
# -*- coding: utf8 -*-

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as log

import accounts.form as form
import accounts.models as model


@login_required
def my_account(request):
    template = loader.get_template('accounts/my_account.html')
    return HttpResponse(template.render(request=request))


def login(request):
    data = {}
    template = loader.get_template('accounts/login.html')
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        print(password, username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            log(request, user)
            print("login ok")
            data = {
                "user_ok" : True
            }
        else :
            print("login nok")
            data = {
                "user_nok" : True
            }
    return HttpResponse(template.render(data, request=request))


@login_required
def logout(request):
    template = loader.get_template('accounts/logout.html')
    return HttpResponse(template.render(request=request))


def join(request):
    data = {}
    template = loader.get_template('accounts/join.html')
    if request.method == 'POST':
        user_raw = {
            "password" : request.POST.get('password'),
            "email" : request.POST.get('email'),
            "username" : request.POST.get('username')
        }
        response = model.create_user(user_raw)
        print(user_raw, response)

    return HttpResponse(template.render(data, request=request))
