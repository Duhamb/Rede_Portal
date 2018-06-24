# Generated by Django 2.0.5 on 2018-06-24 13:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues_report', '0002_auto_20180526_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='people_in_charge',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
