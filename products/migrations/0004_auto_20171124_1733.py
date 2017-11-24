# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171124_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='trending',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
