# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0016_auto_20170810_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecs',
            name='ecs_delete_time',
            field=models.DateTimeField(null=True, verbose_name='删除时间'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='ecs_shut_time',
            field=models.DateTimeField(null=True, verbose_name='关机时间'),
        ),
    ]
