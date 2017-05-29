# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20170529_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(2, 'Ready'), (4, 'Delivered'), (3, 'On the way'), (1, 'Cooking')]),
        ),
    ]
