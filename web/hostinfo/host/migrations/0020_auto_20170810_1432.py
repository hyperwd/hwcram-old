# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0019_auto_20170810_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs',
            name='delete_ecs_tag',
            field=models.BooleanField(default=1, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='shut_ecs_tag',
            field=models.BooleanField(default=1, verbose_name='是否关机'),
        ),
    ]
