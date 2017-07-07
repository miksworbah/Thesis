# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from models import Profile, Skill, Certification, Education, Experience

# Create your views here.
def resume(request):
    profiles = Profile.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    educations = Education.objects.all().order_by('-graduation')
    experiences = Experience.objects.all().order_by('-startdate')
    return render(request, 'resume/resume.html', {'profiles': profiles,
    'skills': skills,'certifications': certifications,'educations': educations,
    'experiences': experiences, })

def homepage(request):
    return render(request, 'resume/homepage.html')
