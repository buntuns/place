# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
