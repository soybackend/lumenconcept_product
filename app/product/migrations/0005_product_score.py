# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='Score'),
        ),
    ]
