# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-24 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20181024_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='site_sighn',
            field=models.CharField(default='', max_length=64),
        ),
    ]