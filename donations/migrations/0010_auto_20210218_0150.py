# Generated by Django 3.0.4 on 2021-02-18 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0009_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='claimed',
        ),
        migrations.CreateModel(
            name='ClaimedDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickupDate', models.DateField()),
                ('claimingOrg', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='donations.Organization')),
                ('contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('donationClaimed', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='donations.Donation')),
            ],
        ),
    ]
