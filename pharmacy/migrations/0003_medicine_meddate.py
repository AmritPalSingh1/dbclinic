# Generated by Django 2.1.4 on 2018-12-29 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_auto_20181228_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='medDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
