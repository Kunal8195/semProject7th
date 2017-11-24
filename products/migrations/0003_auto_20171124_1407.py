# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171028_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='producttype',
            field=models.CharField(max_length=50),
        ),
    ]
