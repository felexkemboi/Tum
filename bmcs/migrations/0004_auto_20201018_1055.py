# Generated by Django 2.1 on 2020-10-18 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bmcs', '0003_upcomingtenders_upload_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingtenders',
            name='upload_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
