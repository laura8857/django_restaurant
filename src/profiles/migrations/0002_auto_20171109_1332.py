# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follower',
            new_name='followers',
        ),
    ]