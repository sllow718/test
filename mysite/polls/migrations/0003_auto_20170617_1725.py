# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170617_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hscode',
            name='description',
            field=models.CharField(max_length=99999),
        ),
        migrations.AlterField(
            model_name='hscode',
            name='hs_code',
            field=models.CharField(max_length=99999),
        ),
        migrations.AlterField(
            model_name='hscode',
            name='serial_no',
            field=models.CharField(max_length=99999),
        ),
    ]