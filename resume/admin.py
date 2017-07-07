# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Profile, Skill, Certification, Education, Experience

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','email','website','citizenship',
    'veteran','sc')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('type','skill')

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('group','certification')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree','major','school','address','graduation','gpa','coursework')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position','company','address','startdate','enddate','time','salary',
    'ksa1','ksa2','ksa3','ksa4','ksa5','ksa6','ksa7','ksa8')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
