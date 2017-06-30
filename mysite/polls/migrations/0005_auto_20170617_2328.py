# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170617_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.CharField(max_length=99999),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.CharField(default='question', max_length=9999, unique=True),
        ),
    ]