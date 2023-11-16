# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_photo_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='seo_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='seo_title',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
