# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantamarconi', '0006_auto_20171205_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organogram',
            name='parent_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantamarconi.Organogram'),
        ),
    ]