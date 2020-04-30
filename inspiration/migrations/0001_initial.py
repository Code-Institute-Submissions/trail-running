# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-30 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('category', models.CharField(choices=[('stories', 'stories'), ('health', 'health'), ('tests', 'tests')], max_length=10)),
                ('title', models.CharField(default='', max_length=254)),
                ('author', models.CharField(default='', max_length=30)),
                ('introduction', models.TextField()),
                ('content_one', models.TextField(blank=True, null=True)),
                ('content_two', models.TextField(blank=True, null=True)),
                ('content_three', models.TextField(blank=True, null=True)),
                ('content_four', models.TextField(blank=True, null=True)),
                ('content_five', models.TextField(blank=True, null=True)),
                ('main_image', models.ImageField(upload_to='inspiration_images')),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='inspiration_images')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='inspiration_images')),
                ('image_three', models.ImageField(blank=True, null=True, upload_to='inspiration_images')),
                ('image_four', models.ImageField(blank=True, null=True, upload_to='inspiration_images')),
                ('image_five', models.ImageField(blank=True, null=True, upload_to='inspiration_images')),
            ],
        ),
    ]
