# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackingSystem', '0002_vehicle_vehicle_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='license_no',
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrackingSystem.Vehicle'),
            preserve_default=False,
        ),
    ]
