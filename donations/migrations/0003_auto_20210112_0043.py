# Generated by Django 3.0.4 on 2021-01-12 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_remove_item_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='number',
        ),
        migrations.RemoveField(
            model_name='item',
            name='typeOfMeasure',
        ),
    ]
