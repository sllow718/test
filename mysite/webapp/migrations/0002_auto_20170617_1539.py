# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 07:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
