# Generated by Django 4.2.6 on 2023-12-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('day_kpi', models.IntegerField(default=0)),
                ('month_kpi', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.data')),
            ],
        ),
    ]
