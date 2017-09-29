# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    stauts = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey(Event)   #关联 发布会ID
    realname = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    isSign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event','phone')

    def __unicode__(self):
        return self.realname