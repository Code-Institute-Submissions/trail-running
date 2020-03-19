# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-19 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0007_auto_20200317_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('xxs', 'XX-Small'), ('xs', 'X-Small'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('xl', 'X-Large'), ('xxl', 'XX-Large'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47')], default='n/a', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discounts.Product'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discounts.Size'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(through='discounts.Item', to='discounts.Size'),
        ),
    ]
