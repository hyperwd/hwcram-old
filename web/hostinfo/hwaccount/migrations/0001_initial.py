# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hwaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=20, verbose_name='账户名')),
                ('user_name', models.CharField(default='使用帐户名登录，此项可留空', max_length=20, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('pid_north1', models.CharField(default='我的凭证中查看项目列表', max_length=40, verbose_name='项目ID-华北1')),
                ('pid_east2', models.CharField(max_length=40, verbose_name='项目ID-华东2')),
                ('pid_south1', models.CharField(max_length=40, verbose_name='项目ID-华南1')),
            ],
        ),
    ]
