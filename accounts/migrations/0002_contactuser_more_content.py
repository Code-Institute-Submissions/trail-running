# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-20 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactuser',
            name='more_content',
            field=models.TextField(default=models.TextField()),
        ),
    ]
