# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hwaccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hwaccount',
            new_name='Account',
        ),
    ]