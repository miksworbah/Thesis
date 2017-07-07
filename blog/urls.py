# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from views import *

# Create your urls here.
urlpatterns = [
    url(r'^blog/$', post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', post_publish, name='post_publish'),
    url(r'^drafts/$', post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', comment_remove, name='comment_remove'),
]
