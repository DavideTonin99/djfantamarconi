# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamarconi', '0011_processes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processes',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255, unique=True)),
        ),
    ]
