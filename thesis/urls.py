
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib.gis import admin
from django.contrib.auth import views

# Create your urls here.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^', include('blog.urls')),
    url(r'^', include('resume.urls')),
    url(r'^', include('wfs.urls')),
    url(r'^', include('ntm.urls')),
]
