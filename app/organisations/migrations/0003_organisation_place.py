# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20161223_1605'),
        ('organisations', '0002_auto_20161128_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='place',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place', to='place.Place', verbose_name='Местро расположения'),
        ),
    ]