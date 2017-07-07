# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from views import *

# Create your urls here.
urlpatterns = [
    url(r'^resume/$', resume, name='resume'),
    url(r'^$', homepage, name='homepage'),
]
