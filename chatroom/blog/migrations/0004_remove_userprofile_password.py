# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160922_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]
