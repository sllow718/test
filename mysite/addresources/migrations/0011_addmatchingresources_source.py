# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0010_auto_20170630_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmatchingresources',
            name='Source',
            field=models.CharField(default='Insert Source', max_length=500),
        ),
    ]
