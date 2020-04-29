# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0003_auto_20200421_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='clothes_size',
            field=models.ForeignKey(blank=True, default=36, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='clothessize', to='discounts.ClothesSize'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shoe_size',
            field=models.ForeignKey(blank=True, default=36, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='shoesize', to='discounts.ShoeSize'),
        ),
    ]