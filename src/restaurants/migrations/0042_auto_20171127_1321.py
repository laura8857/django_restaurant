# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0041_auto_20171126_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='cover_image',
            field=models.ImageField(default='static/media/restaurant_no_cover.jpg', upload_to='static/media/', verbose_name='封面'),
        ),
    ]
