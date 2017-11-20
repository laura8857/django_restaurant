# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-15 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20171105_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=100)),
                ('geolocation', django_google_maps.fields.GeoLocationField(blank=True, max_length=100)),
            ],
        ),
    ]