# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-14 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paking', '0002_auto_20190314_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='in_time',
            field=models.DateTimeField(null=True, verbose_name='驶入时间'),
        ),
        migrations.AlterField(
            model_name='car',
            name='out_time',
            field=models.DateTimeField(null=True, verbose_name='驶出时间'),
        ),
    ]
