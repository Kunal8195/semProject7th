# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171124_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productname', models.CharField(max_length=100)),
                ('producttype', models.CharField(max_length=50)),
                ('availability', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to=b'')),
                ('civil', models.IntegerField()),
                ('csit', models.IntegerField()),
                ('mechanical', models.IntegerField()),
                ('electrical', models.IntegerField()),
                ('electronics', models.IntegerField()),
            ],
        ),
    ]
