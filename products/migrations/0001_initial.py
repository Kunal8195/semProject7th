# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productname', models.CharField(max_length=20)),
                ('producttype', models.CharField(max_length=20)),
                ('availability', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
