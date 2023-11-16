# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20161223_1511'),
        ('organisations', '0003_organisation_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='Название фотографии')),
                ('image', models.ImageField(default='', upload_to='description', verbose_name='Image')),
                ('show', models.BooleanField(default=False, verbose_name='Отображать на сайте')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата размещения')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='коментарии к фотографии')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_organisation', to='article.Article', verbose_name='Привязанная статья')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_organisation', to='organisations.Organisation', verbose_name='Фотография к статье')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_organisation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]