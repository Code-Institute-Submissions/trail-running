# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-31 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='test',
            field=models.IntegerField(null=True),
        ),
    ]