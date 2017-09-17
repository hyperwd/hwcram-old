# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0013_remove_ecs_operate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecs',
            name='id',
        ),
        migrations.AlterField(
            model_name='ecs',
            name='ecs_id',
            field=models.CharField(default='例：c90ab83a-6cdd-4404-8578-05fa965cfb12', max_length=128, primary_key=True, serialize=False, verbose_name='主机ID'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='ecs_name',
            field=models.CharField(default='例：dwx411174_test', max_length=128, verbose_name='主机名称'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='region',
            field=models.CharField(choices=[('华北1', 'cn-north-1'), ('华南1', 'cn-south-1')], default='华北1', max_length=32, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='submitter',
            field=models.CharField(default='填写工号，例：dwx411174', max_length=128, verbose_name='提交人'),
        ),
    ]
