# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0018_ecs_ecs_status_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs',
            name='ecs_status_tag',
            field=models.BooleanField(default=1, verbose_name='是否运行中'),
        ),
    ]