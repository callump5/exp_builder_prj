# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 00:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0005_jobpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='applicants',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
