# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-26 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200526_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=99, null=True),
        ),
    ]
