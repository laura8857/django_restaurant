# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.TextField(blank=True, default='', max_length=250, verbose_name='照片說明'),
        ),
    ]
