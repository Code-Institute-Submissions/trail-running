# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]