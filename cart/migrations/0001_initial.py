# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart_items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.IntegerField()),
                ('price', models.IntegerField()),
                ('productname', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
    ]
