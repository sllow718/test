# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0016_remove_addmatchingresources_catalyst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmatchingresources',
            name='Temperature',
        ),
    ]
