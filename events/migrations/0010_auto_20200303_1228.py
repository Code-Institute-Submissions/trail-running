# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-03 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_day_of_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day_of_month',
            field=models.IntegerField(),
        ),
    ]
