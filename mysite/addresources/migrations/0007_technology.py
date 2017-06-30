# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresources', '0006_auto_20170205_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Method', models.TextField()),
                ('Process', models.TextField()),
                ('add_matchingresources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresources.addmatchingresources')),
                ('add_resources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresources.addresources')),
            ],
        ),
    ]