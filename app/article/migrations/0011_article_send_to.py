# Generated by Django 4.2.3 on 2023-07-04 09:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_article_site_sighn'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='send_to',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None),
        ),
    ]
