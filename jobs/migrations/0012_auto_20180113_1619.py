# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20180113_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
