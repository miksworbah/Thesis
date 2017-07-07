# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ntm import download
from ntm import load
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from serializers import NTMSerializer, PaginatedNTMSerializer
from models import NTM

# Create your views here.
class GIS(TemplateView):
    template_name = 'gis/index.html'

class NTMList(generics.ListCreateAPIView):
    model = NTM
    serializer_class = NTMSerializer
    queryset = NTM.objects.all()
    pagination_class = PaginatedNTMSerializer

ntm_list = NTMList.as_view()

class NTMDetails(generics.RetrieveAPIView):
    queryset = NTM.objects.all()
    serializer_class = NTMSerializer
    lookup_field = 'id'

ntm_details = NTMDetails.as_view()

class NTMDatasets(generics.ListCreateAPIView):
    model = NTM
    serializer_class = NTMSerializer
    queryset = NTM.objects.all()

ntm_datasets = NTMDatasets.as_view()

def downloadntm(request):
    NTM.objects.all().delete()
    download.main()
    load.run()
    return HttpResponseRedirect('/gis/')
