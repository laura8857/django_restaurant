# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0040_auto_20171124_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
