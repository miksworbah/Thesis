# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255)),
                ('certification', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Certifications',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('graduation', models.DateField()),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coursework', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('time', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('ksa1', models.CharField(blank=True, max_length=2000)),
                ('ksa2', models.CharField(blank=True, max_length=2000)),
                ('ksa3', models.CharField(blank=True, max_length=2000)),
                ('ksa4', models.CharField(blank=True, max_length=2000)),
                ('ksa5', models.CharField(blank=True, max_length=2000)),
                ('ksa6', models.CharField(blank=True, max_length=2000)),
                ('ksa7', models.CharField(blank=True, max_length=2000)),
                ('ksa8', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('citizenship', models.CharField(blank=True, max_length=255)),
                ('veteran', models.CharField(blank=True, max_length=255)),
                ('sc', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('skill', models.CharField(max_length=255)),
            ],
        ),
    ]
