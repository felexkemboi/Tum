# Generated by Django 2.1 on 2020-10-18 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmcs', '0005_auto_20201018_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingtenders',
            name='Project_file',
        ),
    ]