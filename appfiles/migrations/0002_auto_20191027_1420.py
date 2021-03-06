# Generated by Django 2.2 on 2019-10-27 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllRoutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('dateCreated', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 14, 20, 28, 875150))),
                ('author', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busName', models.CharField(max_length=100)),
                ('tDate', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 14, 20, 28, 877150))),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tickets',
            name='purchasedTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 14, 20, 28, 872147)),
        ),
    ]
