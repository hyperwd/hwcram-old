# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0008_auto_20170808_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs_all',
            name='operate',
            field=models.BooleanField(default=1),
        ),
    ]
