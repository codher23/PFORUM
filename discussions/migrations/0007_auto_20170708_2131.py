# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0006_auto_20170708_2128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
