# Generated by Django 4.2.6 on 2023-12-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_data_month_kpi'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='month_kpi',
            field=models.IntegerField(default=0),
        ),
    ]