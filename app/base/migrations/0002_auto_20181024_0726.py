# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-24 07:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 7, 26, 14, 278122, tzinfo=utc), verbose_name='Время для архива'),
        ),
        migrations.AlterField(
            model_name='typepage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 7, 26, 14, 278122, tzinfo=utc), verbose_name='Время для архива типов'),
        ),
    ]
