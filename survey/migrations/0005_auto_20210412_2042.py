# Generated by Django 3.1.7 on 2021-04-13 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210410_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
