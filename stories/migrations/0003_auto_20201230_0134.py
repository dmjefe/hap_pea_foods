# Generated by Django 3.0.4 on 2020-12-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
