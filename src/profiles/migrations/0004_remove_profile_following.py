# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171109_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
