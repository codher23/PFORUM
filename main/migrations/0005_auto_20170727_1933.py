# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_activity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]