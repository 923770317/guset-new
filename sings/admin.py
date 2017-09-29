# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','stauts','address','start_time')   #admin 页面显示
    search_fields = ['name','address']   #增加搜索框
    list_filter = ['stauts']   #增加列表筛选框

class GuestAdmin(admin.ModelAdmin):
    list_display = ('realname','phone','email','isSign','event')
    search_fields = ['realname','phone']
    list_filter = ['isSign']

# Register your models here.
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)