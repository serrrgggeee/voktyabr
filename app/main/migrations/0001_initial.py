# Generated by Django 3.0 on 2021-04-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=68, null=True, verbose_name='наименование')),
                ('description', models.TextField(blank=True, max_length=128, null=True, verbose_name='описание')),
                ('keywords', models.TextField(blank=True, max_length=128, null=True, verbose_name='ключевые слова')),
                ('h1', models.TextField(blank=True, max_length=68, null=True, verbose_name='h1')),
            ],
        ),
    ]
