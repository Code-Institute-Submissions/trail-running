# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-15 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20200208_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_image',
        ),
    ]
