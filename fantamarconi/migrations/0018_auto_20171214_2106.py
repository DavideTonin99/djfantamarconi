# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamarconi', '0017_auto_20171214_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processes',
            name='slug',
            field=models.SlugField(),
        ),
    ]