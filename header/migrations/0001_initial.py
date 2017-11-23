# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customernumber', models.CharField(max_length=10)),
                ('customername', models.CharField(max_length=100)),
                ('contactlastname', models.CharField(max_length=100)),
                ('contactfirstname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='customer',
            field=models.ForeignKey(to='header.Customers'),
        ),
    ]
