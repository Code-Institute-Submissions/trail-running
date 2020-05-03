# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-02 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0003_auto_20200502_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('stories', 'stories'), ('health_food', 'health_food'), ('destinations', 'destinations'), ('exercise_injuries', 'exercise_injuries')], max_length=20),
        ),
    ]
