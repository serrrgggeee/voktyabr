# Generated by Django 3.0 on 2021-04-27 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('book', '0004_auto_20210423_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Seo'),
        ),
    ]
