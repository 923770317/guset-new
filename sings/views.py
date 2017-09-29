# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    return render(request,'index.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')  # 重定向
            # response.set_cookie('user',username,3600) # 设置cookie
            request.session['user'] = username
            return response
        else:
            return render(request,'index.html',{'error':'username or password error'})

def event_manage(request):
    # username = request.COOKIES.get('user','')   # 取出cookie
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username})
