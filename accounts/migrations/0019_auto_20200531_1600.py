# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-31 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200531_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuser',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
