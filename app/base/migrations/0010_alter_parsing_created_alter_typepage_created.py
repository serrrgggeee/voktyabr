# Generated by Django 4.2.2 on 2023-07-02 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20210427_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 2, 13, 28, 26, 892598, tzinfo=datetime.timezone.utc), verbose_name='Время для архива'),
        ),
        migrations.AlterField(
            model_name='typepage',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 2, 13, 28, 26, 892309, tzinfo=datetime.timezone.utc), verbose_name='Время для архива типов'),
        ),
    ]
