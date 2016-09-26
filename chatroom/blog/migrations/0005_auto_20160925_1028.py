# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_userprofile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
