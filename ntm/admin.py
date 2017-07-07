# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import NTM
from leaflet.admin import LeafletGeoAdmin
# Optional: from django.contrib.gis.db import OSMGeoAdmin

# Register your models here.
class NTMAdmin(LeafletGeoAdmin):
    list_display = ('chart','action','itemname','chartingla','latitude','longitude',
    'latdd','longdd','publishedd','kapp','rncpanel','rncposted','geom')

admin.site.register(NTM, NTMAdmin)
