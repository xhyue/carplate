# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-18 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0006_standard_time_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='time_unit',
            field=models.CharField(max_length=20, verbose_name='时间单位'),
        ),
    ]