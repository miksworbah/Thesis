# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.pagination import GeoJsonPagination
from models import NTM

# Create your serializers here.
class NTMSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = NTM
        geo_field = "geom"
        fields = ('id','chart', 'action', 'itemname', 'chartingla', 'latitude',
         'longitude', 'latdd', 'longdd', 'publishedd', 'kapp', 'rncpanel',
         'rncposted')

class PaginatedNTMSerializer(GeoJsonPagination):
    page_size_query_param = 'limit'
    page_size = 40
    max_page_size = 10000
