# Generated by Django 2.1 on 2020-10-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmcs', '0006_remove_upcomingtenders_project_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingtenders',
            name='Tender_Id',
        ),
        migrations.AddField(
            model_name='upcomingtenders',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
