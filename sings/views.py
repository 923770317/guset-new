# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

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
    # username = request.session.get('user','')  # 取出 session
    # return render(request,'event_manage.html',{'user':username})
    event_list  = None
    serch_name = request.GET.get('name','')
    if serch_name:
        event_list = Event.objects.filter(name__icontains=serch_name)
    else:
        event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    page = request.GET.get('page')
    guest_list = None
    search_phone = request.GET.get('phone','')
    if search_phone:
        guest_list = Guest.objects.filter(phone__contains=search_phone)
    else:
        guest_list =  Guest.objects.all()
    paginator = Paginator(guest_list,2)
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1) # 如果page 不是整数，则去第一页
    except EmptyPage:
        content = paginator.page(paginator.num_pages)  #如果page 不在范围内，则取最后一页

    return render(request, 'guest_manage.html', {'user': username, 'guests': content})

@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event,id=eid)
    return  render(request,'sign_index.html',{'event':event})

@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone','')
    print phone
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.'})
    result = Guest.objects.get(phone=phone,event_id=eid)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id or ponoe error'})
    if result.isSign:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has sign in'})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(isSign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!','guest':result})

