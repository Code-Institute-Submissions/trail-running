# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-26 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0004_size_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='parent',
        ),
    ]