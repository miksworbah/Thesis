# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import GIS, ntm_list, ntm_details, ntm_datasets, downloadntm

# Create your urls here.
urlpatterns = [
    url(r'^downloadntm/$', downloadntm),
    url(r'^gis/$', GIS.as_view(), name ='gis'),
    url(r'^ntm/$', ntm_list),
    url(r'^ntm/(?P<id>[0-9]+)/$', ntm_details),
    url(r'^ntm_data/$', ntm_datasets, name ='ntm'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
