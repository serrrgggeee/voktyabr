# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-05 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_site_sighn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to='article', verbose_name='Article'),
        ),
    ]
