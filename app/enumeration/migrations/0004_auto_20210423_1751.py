# Generated by Django 3.0 on 2021-04-23 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('place', '0014_auto_20210423_1751'),
        ('enumeration', '0003_enumeration_menu_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enumeration',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='enumeration.Enumeration'),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='place',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place_enumerate', to='place.Place', verbose_name='Местро расположения'),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
