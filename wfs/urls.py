# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from views import global_handler

# Create your urls here.
urlpatterns =[
    url(r'^(?P<service_id>\d+)/$', global_handler, name='wfs'),
    ]
