# Generated by Django 2.1 on 2020-10-18 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmcs', '0002_auto_20201018_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingtenders',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 10, 54, 15, 558955)),
        ),
    ]
