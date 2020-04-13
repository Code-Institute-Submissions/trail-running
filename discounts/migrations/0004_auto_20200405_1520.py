# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-05 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0003_auto_20200404_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category',)},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([]),
        ),
    ]
