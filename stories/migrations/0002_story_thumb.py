# Generated by Django 3.0.4 on 2020-12-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
