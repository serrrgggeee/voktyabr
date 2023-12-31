# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-24 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180508_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ссылка на статью'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('new', 'Новости'), ('pew', 'Спарсиная новость'), ('act', 'Мероприятия'), ('nat', 'Природа'), ('vid', 'Видео')], max_length=3, null=True, verbose_name='тип статьи'),
        ),
    ]
