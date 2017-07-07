# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

class NTM(models.Model):
    chart = models.CharField(max_length=1000)
    action = models.CharField(max_length=1000)
    itemname = models.CharField(max_length=1000)
    chartingla = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)
    latdd = models.CharField(max_length=1000)
    longdd = models.CharField(max_length=1000)
    publishedd = models.CharField(max_length=1000)
    kapp = models.CharField(max_length=1000)
    rncpanel = models.CharField(max_length=1000)
    rncposted = models.CharField(max_length=1000)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.itemname

    class Meta:
        verbose_name_plural = "NTMS"
