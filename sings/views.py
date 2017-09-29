# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    return render(request,'index.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)  #认证用户名和密码
        if user is not None:
            auth.login(request,user) #登录
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            return response
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')  # 重定向
        #     # response.set_cookie('user',username,3600) # 设置cookie
        #     request.session['user'] = username  #设置session
        #     return response
        else:
            return render(request,'index.html',{'error':'username or password error'})

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','')   # 取出cookie
    username = request.session.get('user','')  # 取出 session
    return render(request,'event_manage.html',{'user':username})
