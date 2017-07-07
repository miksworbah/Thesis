# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    website = models.URLField()
    citizenship = models.CharField(max_length=255, blank=True)
    veteran = models.CharField(max_length=255, blank=True)
    sc = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profiles"

class Certification(models.Model):
    group = models.CharField(max_length=255)
    certification = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Certifications"

class Skill(models.Model):
    type = models.CharField(max_length=255)
    skill = models.CharField(max_length=255)

class Education(models.Model):
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    graduation = models.DateField()
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    coursework = models.CharField(max_length=2000)

    class Meta:
        verbose_name_plural = "Educations"

class Experience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    time = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    ksa1 = models.CharField(max_length=2000, blank=True)
    ksa2 = models.CharField(max_length=2000, blank=True)
    ksa3 = models.CharField(max_length=2000, blank=True)
    ksa4 = models.CharField(max_length=2000, blank=True)
    ksa5 = models.CharField(max_length=2000, blank=True)
    ksa6 = models.CharField(max_length=2000, blank=True)
    ksa7 = models.CharField(max_length=2000, blank=True)
    ksa8 = models.CharField(max_length=2000, blank=True)

    class Meta:
        verbose_name_plural = "Experiences"
