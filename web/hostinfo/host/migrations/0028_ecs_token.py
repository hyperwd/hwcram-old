# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host', '0027_auto_20170825_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecs',
            fields=[
                ('ecs_name', models.CharField(default='例：dwx411174_test', max_length=128, verbose_name='主机名称')),
                ('ecs_id', models.CharField(default='例：c90ab83a-6cdd-4404-8578-05fa965cfb12', max_length=40, primary_key=True, serialize=False, verbose_name='主机ID')),
                ('region', models.CharField(choices=[('cn-north-1', '华北1'), ('cn-south-1', '华南1')], default='cn-north-1', max_length=32, verbose_name='区域')),
                ('ecs_shut_time', models.DateTimeField(null=True, verbose_name='关机时间')),
                ('ecs_delete_time', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('shut_ecs_tag', models.BooleanField(default=0, verbose_name='关机')),
                ('delete_ecs_tag', models.BooleanField(default=0, verbose_name='删除')),
                ('ecs_status_tag', models.BooleanField(default=0, verbose_name='运行中')),
                ('account_name', models.CharField(max_length=20, null=True, verbose_name='账户')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('region', models.CharField(max_length=32)),
                ('up_time', models.DateTimeField()),
                ('account_name', models.CharField(max_length=20)),
            ],
        ),
    ]