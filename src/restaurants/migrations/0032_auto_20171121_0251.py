# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 02:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0031_auto_20171121_0224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='restaurant',
        ),
    ]
