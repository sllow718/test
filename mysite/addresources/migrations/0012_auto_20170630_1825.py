# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0011_addmatchingresources_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmatchingresources',
            name='Source',
            field=models.IntegerField(default=0),
        ),
    ]
