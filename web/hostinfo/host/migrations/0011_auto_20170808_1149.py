# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0010_auto_20170808_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs',
            name='ecs_last_time',
            field=models.DateTimeField(),
        ),
    ]