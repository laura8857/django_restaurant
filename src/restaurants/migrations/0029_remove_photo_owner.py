# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0028_auto_20171120_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
    ]
