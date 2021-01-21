# Generated by Django 3.0.4 on 2021-01-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20210112_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='typeOfMeasure',
            field=models.CharField(choices=[('ct', 'Count'), ('gal', 'Gallon'), ('lb', 'Pound'), ('liter', 'Liter'), ('box', 'Box'), ('doz', 'Dozen'), ('case', 'Case')], default='ct', max_length=5),
        ),
    ]