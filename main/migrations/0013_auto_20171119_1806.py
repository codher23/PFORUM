# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-19 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_profile_total_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='hacker_rank_rating',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hacker_rank_username',
        ),
    ]
