# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-12 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_month', models.IntegerField()),
                ('name', models.CharField(default='', max_length=254)),
                ('distance', models.CharField(default='', max_length=254)),
                ('distance_range', models.CharField(default='', max_length=254)),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('valid_until', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='events_images')),
                ('month', models.CharField(default='', max_length=254)),
                ('region', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
