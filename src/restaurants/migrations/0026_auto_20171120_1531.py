# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0025_auto_20171120_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category], verbose_name='種類'),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='地區'),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=120, verbose_name='店名'),
        ),
    ]
