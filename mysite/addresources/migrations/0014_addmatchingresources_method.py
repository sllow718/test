# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0013_auto_20170702_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmatchingresources',
            name='Method',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
