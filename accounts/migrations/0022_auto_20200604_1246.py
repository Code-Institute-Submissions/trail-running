# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-04 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200601_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('optional', 'does it mattter?'), ('male', 'male'), ('female', 'female')], default='who cares?', max_length=10),
        ),
    ]
