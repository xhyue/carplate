# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-14 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paking', '0003_auto_20190314_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='inimg',
            field=models.ImageField(default='', upload_to='', verbose_name='驶入图片'),
        ),
        migrations.AlterField(
            model_name='car',
            name='outimg',
            field=models.ImageField(default='', upload_to='', verbose_name='驶出图片'),
        ),
    ]
