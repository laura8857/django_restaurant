# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20171031_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
