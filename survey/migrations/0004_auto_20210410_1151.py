# Generated by Django 3.0.4 on 2021-04-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210410_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='textAnswer',
            field=models.TextField(null=True),
        ),
    ]