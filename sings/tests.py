# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import *


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id = 4,name='DELL Open Meeting',stauts=True,limit=300,address='changzhou',start_time='2017-10-29 08:00:00')
        Guest.objects.create(id = 6,event_id = 3,realname='梁朝伟',phone='13388886666',email='alen@163.com',isSign=False)

    def tearDown(self):
        pass

    def test_event_model(self):
        result = Event.objects.get(name='DELL Open Meeting')
        self.assertEqual(result.address,'changzhou1q')